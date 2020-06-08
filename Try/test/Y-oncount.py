# _*_ coding:utf-8 _*_
# @Time :2020/6/7 10:29
# @Author :yanxia
import imapclient
import pyzmail
import time
import re
import pymysql
import datetime
import traceback
class Count_online(object):
    def __init__(self):
        self.server=imapclient.IMAPClient('imap.mxhichina.com', ssl=True)
    def get_email(self):
        email_address = "dan.he@360che.com"
        password = "360CHEche"
        today = datetime.datetime.now().strftime('%d-%b-%Y')
        # 邮箱和密码
        self.server.login(email_address, password)
        # 默认已上线的邮箱
        self.server.select_folder('已上线项目', readonly=True)
        # 搜索今天的邮件，打印邮件的UID
        UIDS = self.server.search('ALL')

        for _sm in UIDS:
            result = self.server.fetch(_sm, ['BODY[]'])
            messageObj = pyzmail.PyzMessage.factory(result[_sm][b'BODY[]'])
            subject = messageObj.get_subject()
            print(subject)

if __name__ == '__main__':
    m=Count_online()
    b=m.get_email()
