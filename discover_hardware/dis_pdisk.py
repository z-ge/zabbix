#!/usr/bin/env python
#coding:utf-8
#by:zhan

import sys,os,json

pdisk_list=[]
pdisk_dict={"data":None}
cmd='''/opt/dell/srvadmin/bin/omreport storage pdisk controller=0 | grep ^ID | awk -F ": " '{print $2}' 2>/dev/null'''
local_pdisk=os.popen(cmd).readlines()
for pdisk in local_pdisk:
	n_dict={}
	n_dict["{#DISK_NUM}"]=pdisk.replace("\n", "")
	pdisk_list.append(n_dict)
pdisk_dict["data"]=pdisk_list
jsonStr = json.dumps(pdisk_dict, indent=4)
print jsonStr
