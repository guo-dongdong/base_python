#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @CreateTime    : 2020-05-26 14:02
# @Author  : guoDD
# @Email   : Email
# @File    : basePyMySql

"""
	
"""

import pymysql

# 打开数据库
db = pymysql.connect(
    host = "127.0.0.1",
    port=3306,
    user='root',
    passwd='123456',
    db='runoob_db'
)

# 创建游标
cur = db.cursor()

# # 使用 execute()  方法执行 SQL 查询
# cur.execute("SELECT VERSION()")
#
# # 使用 fetchone() 方法获取单条数据.
# data = cur.fetchone()
#
# print("Database version : %s " % data)

# SQL 插入语句
sql = """INSERT INTO sites (name, url) VALUES ("360", "www.360.com")"""
try:
    # 执行sql语句
    cur.execute(sql)
    # 提交到数据库执行
    db.commit()
except:
    # 如果发生错误则回滚
    db.rollback()

# 关闭数据库连接
db.close()

