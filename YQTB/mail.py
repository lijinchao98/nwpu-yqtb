# coding=utf-8
# smtplib 用于邮件的发信动作
import smtplib
from email.mime.text import MIMEText
# email 用于构建邮件内容
from email.header import Header
# 用于构建邮件头

def send_mail():
    # 发信邮箱
    from_addr = '*********@qq.com'#我用的是QQ邮箱
    password = '*********'#这个你在邮箱的设置界面可以找到，一个邮箱有很多授权码，不唯一

    # 收信方邮箱
    to_addrs = ['************']

    # 发信服务器
    smtp_server = 'smtp.qq.com'#发件邮箱的服务器，网上可以查到，QQ是这个

    # 邮箱正文内容，第一个参数为内容，第二个参数为格式(plain 为纯文本)，第三个参数为编码
    text='每日疫情填报已经填报！'#想发啥发啥
    msg = MIMEText(text,'plain','utf-8')

    # 邮件头信息
    msg['From'] = Header(from_addr)
    msg['To'] = Header(",".join(to_addrs)) 
    msg['Subject'] = Header('自动每日疫情填报')#邮件的标题

    # 开启发信服务，这里使用的是加密传输
    server = smtplib.SMTP_SSL(smtp_server)
    server.connect(smtp_server,465)
    # 登录发信邮箱
    server.login(from_addr, password)
    # 发送邮件
    try:
        server.sendmail(from_addr, to_addrs, msg.as_string())
        print('填报成功')
    except:
        print('提交失败，请重试')
    # 关闭服务器
    server.quit()