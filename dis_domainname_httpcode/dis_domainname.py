#!/usr/bin/env python3
import os
import sys
import json
 
data = {}
tcp_list = []
port_list = []

prog_dir = os.path.dirname(sys.argv[0])
os.chdir(prog_dir)

command = "cat domainname_list | sed 's/\.ncgjj\.com\.cn//g' | sed 's/\./_/g' | sed 's/:\/\//_/g'"
lines = os.popen(command).readlines()
for line in lines:
    port=line.strip('\n')
#   port = line.split(':')[1]
    port_list.append(port)
 
for port in list(set(port_list)):
    port_dict = {}
    port_dict['{#DOMAIN_NAME}'] = port
    tcp_list.append(port_dict)
 
data['data'] = tcp_list
jsonStr = json.dumps(data, sort_keys=True, indent=4)
print(jsonStr)
