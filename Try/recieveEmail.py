#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @CreateTime    : 2020-05-27 13:33
# @Author  : guoDD
# @Email   : Email
# @File    : recieveEmail

"""
	
"""
import poplib
import random
from email.parser import Parser
from email.header import decode_header
from email.utils import parseaddr

'''POP的服务器信息'''
# popHost = input('POP3 server: ')
# email = input('email: ')
# password = input('password: ')
popHost = "pop.139.com"
email = "18298461920@139.com"
password = "Gdd1993__"

'''创建POP3对象，添加用户名密码'''
pop3Server = poplib.POP3(popHost)
pop3Server.user(email)
pop3Server.pass_(password)

'''获取邮件数量和占用空间'''
messageCount,mailboxSize = pop3Server.stat()
print("messageCount: ",messageCount)
print("mailboxSize: ",mailboxSize)

'''获取邮件请求返回状态码，每封邮件的字节大小（b`第几封邮件 此邮件字节大小）'''
response, msgNumoctets, octets = pop3Server.list()
print(response, msgNumoctets, octets)
print(type(msgNumoctets))



'''获取任意一封邮件的邮件对象【第一封的编号为1，不是0】'''
msgIndex = random.randint(1,messageCount)
print(msgIndex)

# 获取第msgIndex封邮件的信息
response,msgLines,octets = pop3Server.retr(msgIndex)
# msgLines中为该邮件的每行数据，先将内容连接成字符串，再转化为email.message.Message对象
msgLinesToStr = b"\r\n".join(msgLines).decode("utf8","ignore")
messageObject = Parser().parsestr(msgLinesToStr)
# print(messageObject)
print(type(messageObject))

# 获取邮件日期
msgDate = messageObject["date"]
print('邮件日期: ',msgDate)


'''解码'''
def decodeMsgHeader(header):
    """
    解码头文件
    :param header: 需解码的内容
    :return:
    """
    value, charset = decode_header(header)[0]
    if charset:
        value = value.decode(charset)
    return value

'''获取邮件发件人实名、邮箱地址'''
senderContent = messageObject["From"]
# parseaddr()函数返回的是一个元组(realname, emailAddress)
senderRealName, senderAdr = parseaddr(senderContent)
# 将加密的名称进行解码
senderRealName = decodeMsgHeader(senderRealName)
print("发件人实名: ",senderRealName)       # 发件人实名
print("发件人邮箱: ",senderAdr)            # 发件人邮箱


'''获取邮件主题'''
msgHeader = messageObject["Subject"]
# 对头文件进行解码
msgHeader = decodeMsgHeader(msgHeader)
print("主题: ",msgHeader)


'''解码内容'''
def decodeBody(msgPart):
    """
    解码内容
   :param msgPart: 邮件某部分
    """
    contentType = msgPart.get_content_type()  # 判断邮件内容的类型,text/html
    textContent = ""
    if contentType == 'text/plain' or contentType == 'text/html':
        content = msgPart.get_payload(decode=True)
        charset = msgPart.get_charset()
        if charset is None:
            contentType = msgPart.get('Content-Type', '').lower()
            position = contentType.find('charset=')
            if position >= 0:
                charset = contentType[position + 8:].strip()
        if charset:
            textContent = content.decode(charset)
    return textContent


"""获取邮件正文内容"""
msgBodyContents = []
if messageObject.is_multipart():  # 判断邮件是否由多个部分构成
    messageParts = messageObject.get_payload()  # 获取邮件附载部分
    for messagePart in messageParts:
        bodyContent = decodeBody(messagePart)
        if bodyContent:
            msgBodyContents.append(bodyContent)
else:
    bodyContent = decodeBody(messageObject)
    if bodyContent:
        msgBodyContents.append(bodyContent)
print(msgBodyContents)




""" 终止POP3服务"""
pop3Server.quit()
