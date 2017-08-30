#/bin/bash
#by:zhan

export PATH=$PATH:/bin:/usr/bin:/sbin:/usr/sbin:/opt/dell/srvadmin/bin:/opt/dell/srvadmin/sbin

tempsid=`echo $1 | tr '_' ' '`
/opt/dell/srvadmin/bin/omreport chassis temps | grep -A 1 "$tempsid" | grep Reading | awk -F ": " '{print $2}' | awk '{print $1}'
