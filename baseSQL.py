#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @CreateTime    : 2020-05-26 11:06
# @Author  : guoDD
# @Email   : Email
# @File    : baseSQL

"""
	
"""
import mysql.connector

mydb = mysql.connector.connect(
    host = "127.0.0.1",             #数据库主机名
    user = "root",                 #用户名
    password = "123456",             #密码
    database = "runoob_db",
)


mycursor = mydb.cursor()
# 创建数据库，展示数据库
# mycursor.execute("CREATE DATABASE runoob_db")
# mycursor.execute("show databases")

# 建表，展示表
# mycursor.execute("CREATE TABLE sites (name VARCHAR(255), url VARCHAR(255))")
# mycursor.execute("show tables")

# 给表添加主键
# mycursor.execute("ALTER TABLE sites ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")

# # 插入数据
# sql = "INSERT INTO sites (name, url) VALUES (%s, %s)"
# val = [
#   ('Google', 'https://www.google.com'),
#   ('Github', 'https://www.github.com'),
#   ('Taobao', 'https://www.taobao.com'),
#   ('stackoverflow', 'https://www.stackoverflow.com/')
# ]
# mycursor.executemany(sql, val)
# mydb.commit()  # 数据表内容有更新，必须使用到该语句
#
# print(mycursor.rowcount, "记录插入成功。")

# 查询
mycursor.execute("select * from sites;")
# myresult = mycursor.fetchall()       # fetchall() 获取所有记录
myresult1 = mycursor.fetchone()      # fetchone() 只获取一条信息

# for x in myresult:
#   print(x)

print(myresult1)