#!/usr/bin/env python

import sys
import socket

if len(sys.argv) < 2:
        print >> sys.stderr, "Usage: %s port" % sys.argv[0]
        sys.exit(1)

host_ip = "127.0.0.1"
host_port = sys.argv[1]

#print host_ip,host_port

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
result = sock.connect_ex((str(host_ip),int(host_port)))
if result == 0:
   print "1"
else:
   print "0"
