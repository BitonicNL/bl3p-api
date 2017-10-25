#! /usr/bin/python


import bl3p

import base64
import ConfigParser
import hashlib
import hmac
import json
import pycurl
import sys
import urllib

try:
    from io import BytesIO
except ImportError:
    from StringIO import StringIO as BytesIO

from datetime import datetime
from time import mktime


def d(j):
	print json.dumps(j, sort_keys=True, indent=4, separators=(',', ': '))

# example:
config = ConfigParser.RawConfigParser()

if len(sys.argv) == 2:
	config.read(sys.argv[1])
else:
	config.read('example.cfg')

public_key = config.get('bl3p', 'public_key') # ........-....-....-....-............
secret_key = config.get('bl3p', 'secret_key') # (long string with a-z/A-Z/0-9 and =)

b = Bl3pApi('https://api.bl3p.eu/1/', public_key, secret_key)

d(b.walletHistory('BTC', 10))

