#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import docker
import json

#client = docker.APIClient(base_url='unix://var/run/docker.sock')
client = docker.from_env()
containerList = client.containers()

containerNameList = []
containerNameDict = {}

def dis_container():
    for i,docker in enumerate(containerList):
        containerName = containerList[i]['Names'][0].replace("/","")
        containerNameList.append({'{#CONTAINERNAME}': containerName})
        containerNameDict['data'] = containerNameList
    container_json = json.dumps(containerNameDict,indent=4)
    print(container_json)
    return container_json

dis_container()
