#!/bin/bash

. /etc/profile

PYDIR=/root/monitor/
LOGDIR=/root/monitor/log/
today=`date +%Y%m%d`
yday=`date -d "1 day ago"  +%Y%m%d`

cd $PYDIR
python3 $PYDIR/Logchart_iostat.py -p $PYDIR/Logchart_iostat.ini
rm -rf $LOGDIR/iostat_$today.html;
zip -r  $LOGDIR/iostat_$yday.zip $LOGDIR/iostat_$yday.html;
python3 $PYDIR/SendEmail.py -p $PYDIR/emailset.ini -f $LOGDIR/iostat_$yday.zip