#!/usr/bin/env python
#coding:utf-8
#by:zhan

import sys,os,json

component_list=[]
component_dict={"data":None}
cmd='''/opt/dell/srvadmin/bin/omreport chassis | grep ":" | sed 1d | awk -F ": " '{print $2}' | sed 's/ /_/'  2>/dev/null'''
local_component=os.popen(cmd).readlines()
for component in local_component:
	n_dict={}
	n_dict["{#P_COMPONENT}"]=component.replace("\n", "")
	component_list.append(n_dict)
component_dict["data"]=component_list
jsonStr = json.dumps(component_dict, indent=4)
print jsonStr
