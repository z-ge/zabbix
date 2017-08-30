#/bin/bash
#by:zhan

export PATH=$PATH:/bin:/usr/bin:/sbin:/usr/sbin:/opt/dell/srvadmin/bin:/opt/dell/srvadmin/sbin

diskid=$1
/opt/dell/srvadmin/bin/omreport storage pdisk controller=0 pdisk="$diskid" | grep ^Status | grep Ok |wc -l
