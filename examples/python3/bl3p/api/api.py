# Unofficial Python 3 Bl3p client exchange api


import base64
import hashlib
import hmac
import json
import requests
import urllib.parse


class Bl3pApi:
    url = None
    pubKey = None
    secKey = None
    verbose = False

    def __init__(self, u, pk, sk):
        self.url = u
        self.pubKey = pk
        self.secKey = sk

    def apiCall(self, path, params):
        post_data = urllib.parse.urlencode(params)

        body = ('%s%c%s' % (path, 0x00, post_data)).encode()

        privkey_bin = base64.b64decode(self.secKey)

        signature_bin = hmac.new(privkey_bin, body, hashlib.sha512)

        signature = base64.b64encode(signature_bin.digest()).decode()

        fullpath = '%s%s' % (self.url, path)

        headers = {
                'Rest-Key': self.pubKey,
                'Rest-Sign': signature
                }

        r = requests.get(fullpath, headers=headers, data=post_data)

        response_code = r.status_code
        if response_code != 200:
            raise Exception('unexpected response code: %d' % response_code)

        return r.json()

    # multiply the btc value (e.g 1.3BTC) with this and round-up/down
    def getBtcMultiplier(self):
        return 100000000

    def getEurMultiplier(self):
        return 100000

    # Add order to your account.
    # @method addOrder
    # @param market         'EUR'
    # @param order_type     'bid' or 'ask'
    #                       bid: used if you want to buy bitcoins
    #                       ask: if you want to sell bitcoins
    # @param order_amount   Amount to order *1e8 (so 1 bitcoin is 100000000)
    # @param order_price    Price of order *1e5 (1 euro is 100000)
    # @return Result of the add order call
    def addOrder(self, market, order_type, order_amount, order_price):
        params = {
            'type' : order_type,
            'amount_int' : order_amount,
            'price_int' : order_price,
            'fee_currency' : 'BTC'
        }
        return self.apiCall('%sEUR/money/order/add' % market, params)

    # Cancel a specific order.
    # @method cancelOrder
    # @param market         'EUR'
    # @param order_id       Id of the order
    # @return Direct resulf of the '<market>/money/order/cancel' call
    def cancelOrder(self, market, order_id):
        params = { 'order_id' : order_id }
        return self.apiCall("%sEUR/money/order/cancel" % market, params)

    # Fetch information about an specific order
    # @method orderInfo
    # @param market         'EUR'
    # @param order_id       Id of the order
    # @return Direct resulf of the '<market>/money/order/result' call
    def orderInfo(self, market, order_id):
        params = { 'order_id' : order_id }
        return self.apiCall("%sEUR/money/order/result" % market, params)

    # Fetch complete orderbook
    # @method fullDepth
    # @param market         'EUR'
    # @return Direct resulf of the '<market>/money/depth/full' call
    def fullDepth(self, market):
        return self.apiCall("%sEUR/money/depth/full" % market, { })

    # Get new deposit address.
    # @method getNewDepositAddress
    # @param market         'EUR'
    # @return new deposit address
    def getNewDepositAddress(self, market):
        return self.apiCall("%sEUR/money/new_deposit_address" % market, { })

    # Get the most recent generated deposit address
    # @method getLastDepositAddress
    # @param market         'EUR'
    # @return most recent generated deposit address
    def getLastDepositAddress(self, market):
        return self.apiCall("%sEUR/money/deposit_address" % market, { })

    # Get the last 1000 trades that where executed before an specific trade_id
    # @method fetchTrades
    # @param market         'EUR'
    # @param trade_id       id of the trade
    # @return array of last 1000 executed trades.
    def fetchLast1000Trades(self, market, trade_id):
        params = { 'trade_id' : trade_id }
        return self.apiCall("%sEUR/money/trades/fetch" % market, params)

    # Get the transaction history
    # @method walletHistory
    # @param currency       currency which currency
    # @param n              how many to retrieve
    # @return array json structure with the transaction history
    def walletHistory(self, currency, n):
        params = { 'currency' : currency, 'recs_per_page' : n }
        return self.apiCall('GENMKT/money/wallet/history', params)

    # Get all open orders.
    # @method getAllActiveOrders
    # @param market         'EUR'
    # @return array of open orders
    def getAllActiveOrders(self, market):
        return self.apiCall("%sEUR/money/orders" % market, { });

    # Get the balances
    # @method getBalances
    # @return array json structure with the wallet balances
    def getBalances(self):
        params = { }
        return self.apiCall('GENMKT/money/info', params)

