#!/usr/bin/env python


import bl3p

import json


def d(j):
    print (json.dumps(j, sort_keys=True, indent=4, separators=(',', ': ')))

def main():
    # example:
    public_key = ''
    secret_key = ''

    b = bl3p.Bl3pApi('https://api.bl3p.eu/1/', public_key, secret_key)
#    b.setVerbose(True)
    '''
    koers_in_eur = 5000
    kapitaal_in_eur = 10000
    btc = round(kapitaal_in_eur / koers_in_eur, 8) # round to 8 decimals
    market = 'BTC'
    order_type = 'bid' # 'bid' (=buy BTC) or 'ask' (=sell BTC)
    order_amount = int(btc * b.getBtcMultiplier()) # 1 BTC = 100000000
    order_price = int(koers_in_eur * b.getEurMultiplier()) # 1 EUR = 100000
    d(b.addOrder(market, order_type, order_amount, order_price))
    '''
    '''
    market = 'BTC'
    order_id = 0
    d(b.cancelOrder(market, order_id))
    '''
    '''
    market = 'BTC'
    order_id = 0
    d(b.orderInfo(market, order_id))
    '''
    '''
    market = 'BTC'
    d(b.fullDepth(market))
    '''
    '''
    market = 'BTC'
    d(b.getNewDepositAddress(market))
    '''
    '''
    market = 'BTC'
    d(b.getLastDepositAddress(market))
    '''
    '''
    market = 'BTC'
    trade_id = 0
    d(b.fetchLast1000Trades(market, trade_id))
    '''
    '''
    currency = 'BTC'
    n = 10
    d(b.walletHistory(currency, n))
    '''
    '''
    market = 'BTC'
    d(b.getAllActiveOrders(market))
    '''
#    '''
    d(b.getBalances())
#    '''


if __name__ == '__main__':
    main()

