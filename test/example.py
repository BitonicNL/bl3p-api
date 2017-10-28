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
    b.setVerbose(True)
    d(b.walletHistory('BTC', 10))


if __name__ == '__main__':
    main()

