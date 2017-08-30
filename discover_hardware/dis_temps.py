#!/usr/bin/env python
#coding:utf-8
#by:zhan

import sys,os,json

temps_list=[]
temps_dict={"data":None}
cmd='''/opt/dell/srvadmin/bin/omreport chassis temps | grep '^Probe Name' | awk -F ": " '{print $2}' | tr ' ' '_' 2>/dev/null'''
local_temps=os.popen(cmd).readlines()
for ptemp in local_temps:
	n_dict={}
	n_dict["{#HW_TEMP}"]=ptemp.replace("\n", "")
	temps_list.append(n_dict)
temps_dict["data"]=temps_list
jsonStr = json.dumps(temps_dict, indent=4)
print jsonStr
