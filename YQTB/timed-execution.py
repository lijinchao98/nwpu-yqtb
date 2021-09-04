#-*- coding: UTF-8 -*- 

from mail import send_mail
from tianbao import yqtb_nwpu
import time
import schedule
#引入schedule



def job():
    yqtb_nwpu()
    send_mail()
#定义一个叫job的函数，函数的功能是执行yqtb_nwpu(),并发邮件提示

#schedule.every(1).minutes.do(job)       #部署每10分钟执行一次job()函数的任务
#schedule.every().hour.do(job)            #部署每×小时执行一次job()函数的任务
schedule.every().day.at("00:10").do(job) #部署在每天的00:10执行job()函数的任务
#schedule.every().monday.do(job)          #部署每个星期一执行job()函数的任务
#schedule.every().monday.at("23:40").do(job)#部署每周六的23:40执行函数的任务

while True:
    schedule.run_pending()
    time.sleep(1)    
#以上都是检查部署的情况，如果任务准备就绪，就开始执行任务。
