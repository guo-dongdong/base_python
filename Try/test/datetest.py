#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @CreateTime    : 2020-06-09 16:17
# @Author  : guoDD
# @Email   : Email
# @File    : datetest

"""
	
"""
import datetime


def get_week_of_month(year, month, day):
    """
    获取指定的某天是某个月中的第几周
    周一作为一周的开始
    """
    end = int(datetime.datetime(year, month, day).strftime("%W"))
    begin = int(datetime.datetime(year, month, 1).strftime("%W"))
    week = end - begin +1
    return week



if __name__ == '__main__':
    print(get_week_of_month(2020, 1, 11))
    print(get_week_of_month(2020, 6, 9))

