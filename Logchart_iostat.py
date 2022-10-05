#!/usr/local/bin/python
# coding: utf-8

# Logchart V1.0.0 for python3
# Log Chart
# Copyright (C) 2017-2017 Kinghow - Kinghow@hotmail.com
# Git repository available at https://github.com/kinghows/Logchart

import getopt
import sys
import configparser
import os
from pyecharts import options as opts
from pyecharts.globals import ThemeType
from pyecharts.charts import Page
from pyecharts.charts import Tab
from pyecharts.charts import Line

def findSubStr_clark(sourceStr, str, i):
    count=0
    rs=0
    for c in sourceStr:
        rs=rs+1
        if(c==str):
            count=count+1
        if(count==i):
            return rs

def chart(chart_type,title,xlist,ylist,datas,style,themetype):

    zdict={}
    for i in range(len(ylist)):
        zdict[ylist[i]]=[]

    for row in datas:
        if row[1] == title:
            zdict[row[2]].append(str(row[3])) 

    if chart_type == 'line':    # 折线图
        if style.setdefault('toolbox_opts_is_show',False):
            toolbox_opts=opts.ToolboxOpts()
        else:
            toolbox_opts=None
                
        if style.setdefault('datazoom_opts',None)=='horizontal':
            datazoom_opts=opts.DataZoomOpts()
        elif style.setdefault('datazoom_opts',None)=='vertical':
            datazoom_opts=opts.DataZoomOpts(orient="vertical")
        elif style.setdefault('datazoom_opts',None)=='inside':
            datazoom_opts=opts.DataZoomOpts(type_="inside")
        else:
            datazoom_opts=None
        
        c = Line(themetype)
        c.set_global_opts(title_opts=opts.TitleOpts(title=title,pos_top=style.setdefault('title_pos_top',None),
                                                                pos_right=style.setdefault('title_pos_right',None)),
                legend_opts=opts.LegendOpts(pos_top=style.setdefault('legend_pos_top',None),
                                            pos_left=style.setdefault('legend_pos_left',None),
                                            pos_right=style.setdefault('legend_pos_right',None)),
                toolbox_opts=toolbox_opts,
                datazoom_opts=datazoom_opts,
                xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=style.setdefault('yaxis_opts_rotate',0),
                                                                       formatter=style.setdefault('xaxis_opts_formatter',"{value}")),
                                                                       axistick_opts=opts.AxisTickOpts(is_align_with_label=True),
                                                                       is_scale=False,
                                                                       boundary_gap=False,),
                yaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(formatter=style.setdefault('yaxis_opts_formatter',"{value}"))),                            
            )
        c.add_xaxis(xlist)
        for i in range(len(ylist)):
            name = ylist[i]
            c.add_yaxis(name, zdict[name],
                markpoint_opts=opts.MarkPointOpts(data=[opts.MarkPointItem(type_=style.setdefault('type_',"max"))]),
                is_smooth=style.setdefault('is_smooth',True),
                label_opts=opts.LabelOpts(is_show=style.setdefault('is_show',False)),
                areastyle_opts=opts.AreaStyleOpts(opacity=style.setdefault('opacity',0))
                ) 
        return c

if __name__=="__main__":
    config_file="Logchart_iostat.ini"
    logfile_directory = ""
    one_logfile = ""
    disk_group = ["sda"]
    monitor_index =["rMB/s","wMB/s","rrqm/s","wrqm/s","r_await","w_await","aqu-sz","rareq-sz","wareq-sz","svctm","util"]
    mutli_chart_type ="tab"
    style = {'themetype':'LIGHT','is_smooth':True,'is_show':False,'opacity':0,'datazoom_opts':'inside','toolbox_opts_is_show':True}

    

    opt, args = getopt.getopt(sys.argv[1:], "p:d:m:g:")
    for o,v in opt:
        if o == "-p":
            config_file = v
        elif o == "-d":
            logfile_directory = v
        elif o == "-m":
            monitor_index = v.split(",")
        elif o == "-g":
            disk_group = v.split(",")

    if len(logfile_directory)==0 and os.path.exists(config_file):
        v =''
        config = configparser.ConfigParser()
        config.read(config_file)
        logfile_directory = config.get("set","logfile_directory")
        disk_group = config.get("set","disk_group").split(",")
        monitor_index = config.get("set","monitor_index").split(",")
        mutli_chart_type = config.get("set", "mutli_chart_type")
        try:
            v=config.get("set","chartstyle")
        except:
            pass
        else:
            if v != '':
                style = eval(v)

    style_themetype=style.setdefault('themetype','WHITE')
    if style_themetype=='WHITE':
        themetype=init_opts=opts.InitOpts(theme=ThemeType.WHITE,width=style.setdefault('Initopts_width',"1000px"), height=style.setdefault('Initopts_height',"600px"))
    elif style_themetype=='LIGHT':
        themetype=init_opts=opts.InitOpts(theme=ThemeType.LIGHT,width=style.setdefault('Initopts_width',"1000px"), height=style.setdefault('Initopts_height',"600px"))
    elif style_themetype=='DARK':
        themetype=init_opts=opts.InitOpts(theme=ThemeType.DARK,width=style.setdefault('Initopts_width',"1000px"), height=style.setdefault('Initopts_height',"600px"))
    elif style_themetype=='CHALK':
        themetype=init_opts=opts.InitOpts(theme=ThemeType.CHALK,width=style.setdefault('Initopts_width',"1000px"), height=style.setdefault('Initopts_height',"600px"))
    elif style_themetype=='ESSOS':
        themetype=init_opts=opts.InitOpts(theme=ThemeType.ESSOS,width=style.setdefault('Initopts_width',"1000px"), height=style.setdefault('Initopts_height',"600px"))
    elif style_themetype=='INFOGRAPHIC':
        themetype=init_opts=opts.InitOpts(theme=ThemeType.INFOGRAPHIC,width=style.setdefault('Initopts_width',"1000px"), height=style.setdefault('Initopts_height',"600px"))
    elif style_themetype=='MACARONS':
        themetype=init_opts=opts.InitOpts(theme=ThemeType.MACARONS,width=style.setdefault('Initopts_width',"1000px"), height=style.setdefault('Initopts_height',"600px"))
    elif style_themetype=='PURPLE_PASSION':
        themetype=init_opts=opts.InitOpts(theme=ThemeType.PURPLE_PASSION,width=style.setdefault('Initopts_width',"1000px"), height=style.setdefault('Initopts_height',"600px"))
    elif style_themetype=='ROMA':
        themetype=init_opts=opts.InitOpts(theme=ThemeType.ROMA,width=style.setdefault('Initopts_width',"1000px"), height=style.setdefault('Initopts_height',"600px"))
    elif style_themetype=='ROMANTIC':
        themetype=init_opts=opts.InitOpts(theme=ThemeType.ROMANTIC,width=style.setdefault('Initopts_width',"1000px"), height=style.setdefault('Initopts_height',"600px"))
    elif style_themetype=='SHINE':
        themetype=init_opts=opts.InitOpts(theme=ThemeType.SHINE,width=style.setdefault('Initopts_width',"1000px"), height=style.setdefault('Initopts_height',"600px"))
    elif style_themetype=='VINTAGE':
        themetype=init_opts=opts.InitOpts(theme=ThemeType.VINTAGE,width=style.setdefault('Initopts_width',"1000px"), height=style.setdefault('Initopts_height',"600px"))
    elif style_themetype=='WALDEN':
        themetype=init_opts=opts.InitOpts(theme=ThemeType.WALDEN,width=style.setdefault('Initopts_width',"1000px"), height=style.setdefault('Initopts_height',"600px"))
    elif style_themetype=='WESTEROS':
        themetype=init_opts=opts.InitOpts(theme=ThemeType.WESTEROS,width=style.setdefault('Initopts_width',"1000px"), height=style.setdefault('Initopts_height',"600px"))
    elif style_themetype=='WONDERLAND':
        themetype=init_opts=opts.InitOpts(theme=ThemeType.WONDERLAND,width=style.setdefault('Initopts_width',"1000px"), height=style.setdefault('Initopts_height',"600px"))
    
    if os.path.exists(logfile_directory):
        filenames=os.listdir(logfile_directory)
        for logfilename in filenames:
            if "iostat_" in logfilename and ".html" not in logfilename and ".zip" not in logfilename :
                logfile = os.path.join(logfile_directory,logfilename)
                htmlfile = logfile + '.html'
                if not os.path.exists(htmlfile):
                    if mutli_chart_type=='page':
                        page = Page()
                    else:
                        page = Tab()
                    xlist=[]
                    datalist=[]
                    title = logfilename[logfilename.index('iostat_')+7:logfilename.index('iostat_')+15]
                    try:
                        srcFile = open(logfile, 'r+')
                        lines = srcFile.readlines()
                
                        for line in lines:
                            if '+' in line:
                                x = line[11:19]
                                xlist.append(x)
                            else:
                                for disk in disk_group:
                                    if disk in line:
                                        for index in monitor_index:
                                            if index =="rMB/s":
                                                keyv = float(line[findSubStr_clark(line,'.',2)+2:findSubStr_clark(line,'.',3)+2].strip())
                                            elif index =="wMB/s":
                                                keyv = float(line[findSubStr_clark(line,'.',3)+2:findSubStr_clark(line,'.',4)+2].strip())
                                            elif index =="rrqm/s":
                                                keyv = float(line[findSubStr_clark(line,'.',4)+2:findSubStr_clark(line,'.',5)+2].strip())
                                            elif index =="wrqm/s":
                                                keyv = float(line[findSubStr_clark(line,'.',5)+2:findSubStr_clark(line,'.',6)+2].strip())
                                            elif index =="r_await":
                                                keyv = float(line[findSubStr_clark(line,'.',8)+2:findSubStr_clark(line,'.',9)+2].strip())
                                            elif index =="w_await":
                                                keyv = float(line[findSubStr_clark(line,'.',9)+2:findSubStr_clark(line,'.',10)+2].strip())
                                            elif index =="aqu-sz":
                                                keyv = float(line[findSubStr_clark(line,'.',10)+2:findSubStr_clark(line,'.',11)+2].strip())
                                            elif index =="rareq-sz":
                                                keyv = float(line[findSubStr_clark(line,'.',11)+2:findSubStr_clark(line,'.',12)+2].strip())
                                            elif index =="wareq-sz":
                                                keyv = float(line[findSubStr_clark(line,'.',12)+2:findSubStr_clark(line,'.',13)+2].strip())
                                            elif index =="svctm":
                                                keyv = float(line[findSubStr_clark(line,'.',13)+2:findSubStr_clark(line,'.',14)+2].strip())
                                            elif index =="util":
                                                keyv = float(line[findSubStr_clark(line,'.',14)+2:findSubStr_clark(line,'.',15)+2].strip())

                                            data = []
                                            data.append(x)
                                            data.append(disk)
                                            data.append(index)
                                            data.append(keyv)
                                            datalist.append(data)
                    except:
                        print(logfile+' Some lines are incorrectly formatted，maybe not write finish.')
                    finally:
                        srcFile.close()

                    for disk in disk_group:
                        if mutli_chart_type=='page':
                            page.add(chart('line',disk,xlist,monitor_index,datalist,style,themetype))
                        else:
                            page.add(chart('line',disk,xlist,monitor_index,datalist,style,themetype),disk)
                    page.render(path=htmlfile)
    else:   
        print('Please check '+logfile_directory+' exists!')

