#/bin/bash
#by:zhan
export PATH=$PATH:/bin:/usr/bin:/sbin:/usr/sbin:/opt/dell/srvadmin/bin:/opt/dell/srvadmin/sbin

componentid=`echo $1 | sed 's/_/ /'`
/opt/dell/srvadmin/bin/omreport chassis | grep ": " |sed 1d | grep "$componentid" | grep Ok |wc -l

