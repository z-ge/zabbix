#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import urllib3
import certifi
import sys

if len(sys.argv) < 2:
    print("Usage: %s web_url" % sys.argv[0])
    print("example: %s http://www.baidu.com" % sys.argv[0])
    sys.exit(1)

weburl = sys.argv[1]
http = urllib3.PoolManager(cert_reqs='CERT_REQUIRED',ca_certs=certifi.where())
try:
    r = http.request('GET',weburl,retries=2,timeout=3.0)
except urllib3.exceptions.HTTPError:
    print('Connection failed.')
else:
    print(r.status)
