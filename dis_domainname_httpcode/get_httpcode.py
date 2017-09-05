#!/usr/bin/env python3

import os
import sys
import urllib3
import certifi

prog_dir = os.path.dirname(sys.argv[0])
os.chdir(prog_dir)

url_tag = sys.argv[1]

url = ((url_tag.replace('https_','https://')).replace('http_','http://')).replace('_','.') + ".ncgjj.com.cn"

def check_http(weburl):
    http = urllib3.PoolManager(cert_reqs='CERT_REQUIRED',ca_certs=certifi.where())
    try:
        r = http.request('GET',weburl,retries=2,timeout=3.0)
    except urllib3.exceptions.HTTPError:
        print('555')
    else:
        print(r.status)

check_http(url)
