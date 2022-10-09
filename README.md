# Logchart
Export log to HTML chart.  

chart used pyecharts 1.6+

pip install pyecharts

### Logchart.ini: 
logfile_directory 

monitor_index

### execute:
use Logchart.ini:

python Logchart.py

or 

input parameters:

python Logchart.py -d D:\GitHub\log 

python Logchart.py -d D:\GitHub\log -m "cn_flush_bio,total write bio"

python Logchart_iostat.py -d D:\GitHub\log -m "rMB/s,wMB/s,r_await,w_await,svctm,util" -g "dm-5,dm-6"

Enjoy it!

### iomon:

yum install dstat

yum install sysstat -y

mkdir -p /root/monitor/log

chmod +x /root/monitor/iomon.sh

crontab -e

0 0 * * * /bin/bash /root/monitor/iomon.sh >>/root/monitor/iomon.log

0 0 * * * /bin/bash /root/monitor/iomon_email.sh >>/root/monitor/iomon_email.log




### exe:
pyinstaller --add-data=".\datasets;pyecharts\datasets." --add-data=".\templates;pyecharts\render\templates." -F -w Logchart.py

pyinstaller --add-data=".\datasets;pyecharts\datasets." --add-data=".\templates;pyecharts\render\templates." -F -w Logchart_dstat.py

pyinstaller --add-data=".\datasets;pyecharts\datasets." --add-data=".\templates;pyecharts\render\templates." -F -w Logchart_iostat.py

## 好用的DBA系列，喜欢的请打颗星：

- [MySQL_Watcher：数据库性能指标的HTML监控报告](https://github.com/kinghows/MySQL_Watcher)

- [SQL_Report：自定义SQL生成HTML报告](https://github.com/kinghows/SQL_Report)

- [SQL_Chart：自定义SQL生成HTML图表](https://github.com/kinghows/SQL_Chart)

- [Logthin：日志精简工具](https://github.com/kinghows/Logthin)

- [Logchart：日志图形化工具](https://github.com/kinghows/Logchart)

- [Linux_Report：自定义Linux 命令生成HTML报告](https://github.com/kinghows/Linux_Report)
