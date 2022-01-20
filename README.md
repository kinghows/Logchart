# Logchart
Export log to HTML chart.  

chart used pyecharts 1.6+

pip install pyecharts

### Logchart.ini: 
logfile_directory 
monitor_index

### execute:

python logchart.py -d D:\GitHub\Logchart -m cn_flush_bio,total write bio,total read bio


### send email:

python SendEmail.py -p emailset.ini -f my_chart1.html,my_chart2.html

use crontab regularly perform sql_chart.sh,auto generate html chart,and send email.

Enjoy it!

中文处理Linux需要encode，decode：

88行：

cols.append(str(col).encode('raw_unicode_escape').decode('utf-8')) #linux

#cols.append(str(col)) #windows

105行：

strlist.append(str(col).encode('raw_unicode_escape').decode('utf-8')) #linux

#strlist.append(str(col)) #windows

地理坐标系pyecharts在Linux上有BUG，请设置switch = OFF

## 好用的DBA系列，喜欢的请打颗星：

- [MySQL_Watcher：数据库性能指标的HTML监控报告](https://github.com/kinghows/MySQL_Watcher)

- [SQL_Report：自定义SQL生成HTML报告](https://github.com/kinghows/SQL_Report)

- [SQL_Chart：自定义SQL生成HTML图表](https://github.com/kinghows/SQL_Chart)

- [Logthin：日志精简工具](https://github.com/kinghows/Logthin)

- [Linux_Report：自定义Linux 命令生成HTML报告](https://github.com/kinghows/Linux_Report)
