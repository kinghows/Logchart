#!/bin/bash

. /etc/profile

LOGDIR=/root/monitor/log/
[ -d $LOGDIR ] || mkdir -p $LOGDIR

SUFFIX=`date +%Y%m%d`
INTV=10
CNT=8640

/usr/bin/dstat -cmdnylst $INTV $CNT >> $LOGDIR/dstat_$SUFFIX &
/usr/bin/iostat -mdx $INTV $CNT |awk '/^sd*|^dm*/'|awk -v CTIME=$CTIME '{ print $0,CTIME}' >> $LOGDIR/iostat_$SUFFIX &

find $LOGDIR -mtime +30 -name "dstat_*" -exec rm -rf {} \;
find $LOGDIR -mtime +30 -name "iostat_*" -exec rm -rf {} \;
