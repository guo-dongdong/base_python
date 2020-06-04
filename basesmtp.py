#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @CreateTime    : 2020-05-26 14:30
# @Author  : guoDD
# @Email   : Email
# @File    : basesmtp

import smtplib
from email.mime.multipart import MIMEMultipart
from email.header import Header
from email.mime.text import MIMEText

# SMTP_SSL("邮箱地址", 465/25) 例：smtp.qq.com、smtp.163.com
con = smtplib.SMTP_SSL("smtp.qq.com", 465)

# 注意，如果使用qq邮箱必须申请授权码，163邮箱直接输入用户名和密码即可
con.login("1097765642@qq.com", "jjbnsihwtgbgbafh")

msg = MIMEMultipart()
to = "876417305@qq.com"     #"2446055893@qq.com"                               # 目标邮箱地址 多个用;分开xxx@qq.com;xxx@qq.com;xxx@qq.com
msg["Subject"] = Header("test标题", "utf-8").encode()             # 标题
msg["From"] = "1097765642@qq.com <1097765642@qq.com>"           # 自己邮箱地址
msg["To"] = to                                                  # 目标邮箱地址
content = """
<h1>这是一封测试邮件！！</h1>
"""
html = MIMEText(content, "html", "utf-8") # MIMEText("内容", "类型", "编码方式") 类型：plain、html、base64
msg.attach(html)
con.sendmail("1097765642@qq.com", to, msg.as_string()) # endmail("自己邮箱地址", "目标邮箱地址", msg.as_string())
con.quit()