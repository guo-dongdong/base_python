#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @CreateTime    : 2020-05-27 9:33
# @Author  : guoDD
# @Email   : Email
# @File    : baseWechat

"""
	
"""
from wxpy import *
import itchat

# 创建一个微信机器人,选择缓存模式（扫码）登录
bot = Bot()             # cache_path=True

# 获取好友信息
friend = bot.chats()
print(friend)

# 查找好友并发送消息
my_friend = bot.friends().search('郭丶',sex=MALE)

print(my_friend)
if len(my_friend) == 1:
    # 发送微信消息
    my_friend[0].send("哈喽！")