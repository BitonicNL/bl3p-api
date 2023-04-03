#! /usr/bin/python

# this code was written by folkert@vanheusden.com
# it has been released under AGPL v3.0

# it was updated from python2 to python3 by alain@brutesque.com
# and has been altered to use python-requests library instead of pycurl

import base64
import configparser
import hashlib
import hmac
import sys
import time
from pprint import pprint
from urllib.parse import urlencode

import requests


class Bl3pApi:
    url = None
    pubKey = None
    secKey = None

    def __init__(self, u, pk, sk):
        self.url = u
        self.pubKey = pk
        self.secKey = sk

    @staticmethod
    def nonce():
        """
        Returns a nonce
        Used in authentication
        """
        return str(int(time.time() * 1000000))

    def api_call(self, path, params):
        params['nonce'] = self.nonce()
        encoded_payload = urlencode(params)

        message = '{:s}{:c}{:s}'.format(path, 0x00, encoded_payload)

        h = hmac.new(
            key=base64.b64decode(self.secKey),
            msg=message.encode(),
            digestmod=hashlib.sha512
        )
        signature = h.digest()

        headers = {
            'Rest-Key': self.pubKey,
            'Rest-Sign': base64.b64encode(signature).decode(),
        }

        response = requests.request(
            method='POST',
            url='{}{}'.format(self.url, path),
            data=params,
            headers=headers,
            timeout=(5, 10),
            allow_redirects=False,
            verify=True,
        )
        if response.status_code != 200:
            raise Exception('unexpected response code: %d' % response.status_code)

        return response.json()

    # multiply the btc value (e.g 1.3BTC) with this and round-up/down
    @staticmethod
    def get_btc_multiplier():
        return 100000000

    @staticmethod
    def get_eur_multiplier():
        return 100000

    # Add order to your account.
    # @method add_order
    # @param  market        'EUR'
    # @param  order_type   	'bid' or 'ask'
    #                       bid: used if you want to buy bitcoins
    #                       ask: if you want to sell bitcoins
    # @param  order_amount 	Amount to order *1e8 (so 1 bitcoin is 100000000)
    # @param  order_price  	Price of order *1e5 (1 euro is 100000)
    # @return Result of the add order call
    def add_order(self, market, order_type, order_amount, order_price):
        params = {
            'type': order_type,
            'amount_int': order_amount,
            'price_int': order_price,
            'fee_currency': 'BTC'
        }

        return self.api_call('%sEUR/money/order/add' % market, params)

    # Cancel a specific order.
    # @method cancel_order
    # @param  market        'EUR'
    # @param  order_id 	Id of the order
    # @return Direct result of the '<market>/money/order/cancel' call
    def cancel_order(self, market, order_id):
        params = {'order_id': order_id}

        return self.api_call("%sEUR/money/order/cancel" % market, params)

    # Fetch information about an specific order
    # @method order_info
    # @param  market        'EUR'
    # @param  order_id 	Id of the order
    # @return Direct result of the '<market>/money/order/result' call
    def order_info(self, market, order_id):
        params = {'order_id': order_id}

        return self.api_call("%sEUR/money/order/result" % market, params)

    # Fetch complete orderbook
    # @method full_depth
    # @param  market        'EUR'
    # @return Direct result of the '<market>/money/depth/full' call
    def full_depth(self, market):
        return self.api_call("%sEUR/money/depth/full" % market, {})

    # Get new deposit address.
    # @method get_new_deposit_address
    # @param  market        'EUR'
    # @return new deposit address
    def get_new_deposit_address(self, market):
        return self.api_call("%sEUR/money/new_deposit_address" % market, {})

    # Get the most recent generated deposit address
    # @method get_last_deposit_address
    # @param  market        'EUR'
    # @return most recent generated deposit address
    def get_last_deposit_address(self, market):
        return self.api_call("%sEUR/money/deposit_address" % market, {})

    # Get the last 1000 trades that where executed before an specific trade_id
    # @method fetch_last_1000_trades
    # @param  market        'EUR'
    # @param  trade_id    id of the trade
    # @return array of last 1000 executed trades.
    def fetch_last_1000_trades(self, market, trade_id):
        params = {'trade_id': trade_id}

        return self.api_call("%sEUR/money/trades/fetch" % market, params)

    # Get the transaction history
    # @method wallet_history
    # @param  currency  currency which currency
    # @param  n         how many to retrieve
    # @return array   json structure with the transaction history
    def wallet_history(self, currency, n):
        params = {'currency': currency, 'recs_per_page': n}

        return self.api_call('GENMKT/money/wallet/history', params)

    # Get all open orders.
    # @method get_all_active_orders
    # @param  market        'EUR'
    # @return array of open orders
    def get_all_active_orders(self, market):
        return self.api_call("%sEUR/money/orders" % market, {})

    # Get the balances
    # @method get_balances
    # @return array   json structure with the wallet balances
    def get_balances(self):
        params = {}
        return self.api_call('GENMKT/money/info', params)


# example:
config = configparser.RawConfigParser()

if len(sys.argv) == 2:
    config.read(sys.argv[1])
else:
    config.read('example.cfg')

public_key = config.get('bl3p', 'public_key')  # ........-....-....-....-............
secret_key = config.get('bl3p', 'secret_key')  # (long string with a-z/A-Z/0-9 and =)

b = Bl3pApi('https://api.bl3p.eu/1/', public_key, secret_key)

pprint(b.get_balances())
