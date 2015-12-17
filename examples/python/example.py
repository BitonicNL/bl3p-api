#! /usr/bin/pyton

# this code was written by folkert@vanheusden.com
# it has been released under AGPL v3.0

# it requires 'pycurl'
# in debian this can be found in the 'python-pycurl' package

import base64
try:
    from io import BytesIO
except ImportError:
    from StringIO import StringIO as BytesIO
from datetime import datetime
import hashlib
import hmac
import json
import pycurl
from time import mktime
import urllib

class Bl3pApi:
	url = None
	pubKey = None
	secKey = None
	verbose = False

	def __init__(self, u, pk, sk):
		self.url = u
		self.pubKey = pk
		self.secKey = sk

	def setVerbose(self, v):
		self.verbose = v

	def apiCall(self, path, params):
		dt = datetime.utcnow()
		us = mktime(dt.timetuple()) * 1000 * 1000 + dt.microsecond
		nonce = '%d' % us

		# generate the POST data string
		post_data = urllib.urlencode(params)

		body = '%s%c%s' % (path, 0x00, post_data)

		privkey_bin = base64.b64decode(self.secKey)

		signature_bin = hmac.new(privkey_bin, body, hashlib.sha512).digest()

		signature = base64.b64encode(signature_bin)

		fullpath = '%s%s' % (self.url, path)

		headers = [ 'Rest-Key: %s' % self.pubKey, 'Rest-Sign: %s' % signature ]

		buffer = BytesIO()

		c = pycurl.Curl()
		c.setopt(c.USERAGENT, 'Mozilla/4.0 (compatible; BL3P Python client written by folkert@vanheusden.com; 0.1)');
		c.setopt(c.WRITEFUNCTION, buffer.write)
		c.setopt(c.URL, fullpath);
		c.setopt(c.POST, 1);
		c.setopt(c.POSTFIELDS, post_data);
		c.setopt(c.HTTPHEADER, headers);
		c.setopt(c.SSLVERSION, 1);
		c.setopt(c.SSL_VERIFYPEER, True);
		c.setopt(c.SSL_VERIFYHOST, 2);
		c.setopt(c.CONNECTTIMEOUT, 5);
		c.setopt(c.TIMEOUT, 10);

		if self.verbose:
			c.setopt(c.VERBOSE, 1)
		else:
			c.setopt(c.VERBOSE, 0)

		c.perform()

		response_code = c.getinfo(c.RESPONSE_CODE)
		if response_code != 200:
			raise Exception('unexpected response code: %d' % response_code)

		c.close()

		return json.loads(buffer.getvalue())

	# Get the transaction history
	# @method walletHistory
	# @param  currency  currency which currency
	# @param  n         how many to retrieve
	# @return array   json structure with the transaction history
	def walletHistory(self, currency, n):
		params = { 'currency' : currency, 'recs_per_page' : n }

		return self.apiCall('GENMKT/money/wallet/history', params)

# example:

public_key = 'YOUR PUBLIC KEY' # ........-....-....-....-............
secret_key = 'YOUR SECRET KEY' # (long string with a-z/A-Z/0-9 and =)

b = Bl3pApi('https://api.bl3p.eu/1/', public_key, secret_key)

print json.dumps(b.walletHistory('BTC', 10))
