#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import docker
import sys
import subprocess
import os
import json 

def check_container_stats(container_name,collect_item):
    container_collect = docker_client.stats(container_name,decode=False,stream=True)
    old_result = json.loads(next(container_collect))
    new_result = json.loads(next(container_collect))
    container_collect.close()

    if collect_item == 'cpu_total_usage':
        result = new_result['cpu_stats']['cpu_usage']['total_usage'] - old_result['cpu_stats']['cpu_usage']['total_usage']
    elif collect_item == 'cpu_system_usage':
        result = new_result['cpu_stats']['system_cpu_usage'] - old_result['cpu_stats']['system_cpu_usage']
    elif collect_item == 'cpu_percent':
        cpu_total_usage=new_result['cpu_stats']['cpu_usage']['total_usage'] - old_result['cpu_stats']['cpu_usage']['total_usage']
        cpu_system_uasge=new_result['cpu_stats']['system_cpu_usage'] - old_result['cpu_stats']['system_cpu_usage']
        cpu_num = len(old_result['cpu_stats']['cpu_usage']['percpu_usage'])
        result = round((float(cpu_total_usage)/float(cpu_system_uasge))*cpu_num*100.0,2)
    elif collect_item == 'mem_usage':
        result = new_result['memory_stats']['usage']
    elif collect_item == 'mem_limit':
        result = new_result['memory_stats']['limit']
    elif collect_item == 'network_rx_bytes':
        result = new_result['networks']['eth0']['rx_bytes']
    elif collect_item == 'rx_errors':
        result = new_result['networks']['eth0']['rx_errors']
    elif collect_item == 'network_tx_bytes':
        result = new_result['networks']['eth0']['tx_bytes']
    elif collect_item == 'tx_errors':
        result = new_result['networks']['eth0']['tx_errors']
    elif collect_item == 'mem_percent':
        mem_usage = new_result['memory_stats']['usage']
        mem_limit = new_result['memory_stats']['limit']
        result = round(float(mem_usage)/float(mem_limit)*100.0,2)
    return result

if __name__ == "__main__":
    #docker_client = docker.APIClient(base_url='unix://var/run/docker.sock')
    docker_client = docker.from_env()
    container_name = sys.argv[1]
    collect_item = sys.argv[2]
    print(check_container_stats(container_name,collect_item))
