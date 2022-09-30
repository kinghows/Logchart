#!/bin/bash

. /etc/profile

LOGDIR=/root/monitor/log/
[ -d $LOGDIR ] || mkdir -p $LOGDIR

SUFFIX=`date +%Y%m%d`
CTIME=`date +%H:%M:%S`
INTV=10
CNT=8640
export S_TIME_FORMAT='ISO'

/usr/bin/dstat -cmdnylst $INTV $CNT >> $LOGDIR/dstat_$SUFFIX &
/usr/bin/iostat -mdxt $INTV $CNT |awk '/+0800$|^dm-[456]/' >> $LOGDIR/iostat_$SUFFIX &

find $LOGDIR -mtime +30 -name "dstat_*" -exec rm -rf {} \;
find $LOGDIR -mtime +30 -name "iostat_*" -exec rm -rf {} \;
