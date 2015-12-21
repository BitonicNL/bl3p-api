<?php
/**
  *Make call to the BL3P API
  *@author Roy van Zanten <roy@bitonic.nl>
 */
class Bl3pApi {

	private $pubkey;
	private $privkey;
	private $url;

	/**
	 * Set the url to call, the public key and the private key
	 * @method __construct
	 * @param string $url     Url to call (https://api.bl3p.eu)
	 * @param string $pubkey  Your Public API key
	 * @param string $privkey Your Private API key
	 */
	function __construct($url, $pubkey, $privkey) {
		$this->url = $url;
		$this->pubkey = $pubkey;
		$this->privkey = $privkey;
	}

	/**
	 * To make a call to BL3P API
	 * @method apiCall
	 * @param  string $path   path to call
	 * @param  array  $params parameters to add to the call
	 * @return array          result of call
	 */
	public function apiCall($path, $params=array()) {

		// generate a nonce as microtime, with as-string handling to avoid problems with 32bits systems
		$mt = explode(' ', microtime());
		$vars['nonce'] = $mt[1].substr($mt[0], 2, 6);

		// generate the POST data string
		$post_data = http_build_query($params, '', '&');
		$body = $path . chr(0). $post_data;

		//build signature for Rest-Sign
		$sign = base64_encode(hash_hmac('sha512', $body, base64_decode($this->privkey), true));

		//combine the url and the desired path
		$fullpath = $this->url . $path;

		//set headers
		$headers = array(
			'Rest-Key: '.$this->pubkey,
			'Rest-Sign: '. $sign,
		);

		//build curl call
		$ch = curl_init();
		curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
		curl_setopt($ch, CURLOPT_USERAGENT, 'Mozilla/4.0 (compatible; BL3P PHP client; '.php_uname('s').'; PHP/'.phpversion().')');
		curl_setopt($ch, CURLOPT_URL, $fullpath);
		curl_setopt($ch, CURLOPT_POSTFIELDS, $post_data);
		curl_setopt($ch, CURLOPT_HTTPHEADER, $headers);
		curl_setopt($ch, CURLOPT_SSLVERSION, 1);
		curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, true);
		curl_setopt($ch, CURLOPT_SSL_VERIFYHOST, 2);
		curl_setopt($ch, CURLOPT_CONNECTTIMEOUT, 5);
		curl_setopt($ch, CURLOPT_TIMEOUT, 10);

		//execute curl request
		$res = curl_exec($ch);

		//throw exception with additional information when curl request returns false
		if ($res === false) {
			throw new Exception("API request failed: Could not get reply from API: ".curl_error($ch));
		}

		//close curl connection
		curl_close ($ch);

		//convert json into an array
		$result = json_decode($res, true);

		//check json convert result and throw an exception if invalid
		if (!$result) {
			throw new Exception("API request failed: Invalid JSON-data received: ".substr($res,0,100));
		}

		//check returned result of call, if not success then throw an exception with additional information
		if ($result['result'] !== 'success') {
			if (!isset($json['data']['code']) || !isset($result['data']['message']))
				throw new Exception(sprintf('Received unsuccessful state, and additionally a malformed response: %s', var_export($result['data'], true)));

			throw new Exception(sprintf("API request unsuccessful: [%s] %s", $result['data']['code'], $result['data']['message']));
		}

		return $result;
	}
}

/**
 * ===================================================
 *  Code to make calls with help of the Bl3pApi class
 * ===================================================
 **/

$url = "https://api.bl3p.eu/1/";
$pubkey = "YOUR_PUBLIC_API_KEY";
$privkey = "YOUR_PRIVATE_API_KEY";

//Init Bl3pAPi class
$api = new Bl3pApi($url, $pubkey, $privkey);

try {

	//Add an buy order for 0.01 @400 euro

	$result = addOrder('bid', 1000000, 40000000);

	echo '<tt><pre>'.var_export($result, true) . '</pre></tt>';
} catch (Exception $ex) {
	echo '<tt><pre>'.var_export($ex, true) . '</pre></tt>';
}

/**
 * Add order to your account.
 * @method addOrder
 * @param  string   $order_type    	'bid' or 'ask'
 * @param  int   	$order_amount 	Amount to order *1e8
 * @param  int   	$order_price  	Price of order *1e5
 * @return array 					Result of the add order call
 */

function addOrder($order_type, $order_amount, $order_price) {

	global $api;

	$params = array(
		'type' => $order_type,
		'amount_int' => $order_amount,
		'price_int' => $order_price,
		'fee_currency' => 'BTC'
	);

	$result = $api->apiCall("BTCEUR/money/order/add", $params);

	return $result;
}

/**
 * Cancel a specific order.
 * @method cancelOrder
 * @param  int      $order_id 	Id of the order
 * @return array    			Direct resulf of the '<market>/money/order/cancel' call
 */

function cancelOrder($order_id) {

	global $api;

	$params = array(
		'order_id' => $order_id
	);

	return $api->apiCall("BTCEUR/money/order/cancel", $params);
}

/**
 * Fetch information about an specific order
 * @method orderInfo
 * @param  int    $order_id 	Id of the order
 * @return array            	Direct resulf of the '<market>/money/order/result' call
 */

function orderInfo($order_id) {

	global $api;

	$params = array(
		'order_id' => $order_id
	);

	return $api->apiCall("BTCEUR/money/order/result", $params);
}

/**
 * Fetch complete orderbook
 * @method fullDepth
 * @return array            	Direct resulf of the '<market>/money/depth/full' call
 */

function fullDepth() {

	global $api;

	return $api->apiCall("BTCEUR/money/depth/full");
}

/**
 * Get new deposit address.
 * @method getNewDepositAddress
 * @return array               new deposit address
 */

function getNewDepositAddress() {

	global $api;

	return $api->apiCall("BTCEUR/money/new_deposit_address");
}

/**
 * Get the most recent generated deposit address
 * @method getLastDepositAddress
 * @return array                most recent generated deposit address
 */

function getLastDepositAddress() {

	global $api;

	return $api->apiCall("BTCEUR/money/deposit_address");
}

/**
 * Get the last 1000 trades that where executed before an specific trade_id
 * @method fetchTrades
 * @param  int      $trade_id    id of the trade
 * @return array                 array of last 1000 executed trades.
 */

function fetchLast1000Trades($trade_id) {

	global $api;

	$params = array(
		'trade_id' => $trade_id
	);

	return $api->apiCall("BTCEUR/money/trades/fetch", $params);
}

/**
 * Get the transaction history
 * @method walletHistory
 * @param  string        $currency 	type of currency
 * @return array                    array of transactions
 */

function walletHistory($currency) {

	global $api;

	$params = array(
		'currency' => $currency,
		'recs_per_page' => 25
	);

	return $api->apiCall("GENMKT/money/wallet/history", $params);
}


/**
 * Get all open orders.
 * @method getAllActiveOrders
 * @return array             array of open orders
 */

function getAllActiveOrders(){

	global $api;

	return $api->apiCall("BTCEUR/money/orders");
}
