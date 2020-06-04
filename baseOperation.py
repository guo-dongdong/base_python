#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @CreateTime    : 2020-06-02 14:26
# @Author  : guoDD
# @Email   : Email
# @File    : baseOperation

"""
	
"""

class OperateElement:
    def __init__(self,driver):
        self.driver = driver

    # 向上滑动
    def swipeToUp(self):
        window = self.driver.get_window_size()
        x = window["width"] * 0.5  # 保持横坐标不变
        y1 = window["height"] * 0.8  # 起始纵坐标
        y2 = window["height"] * 0.2  # 终止纵坐标
        self.driver.swipe(x, y1, x, y2)

    # 向下滑动
    def swipeToDown(self):
        window = self.driver.get_window_size()
        x = window["width"] * 0.5  # 保持横坐标不变
        y1 = window["height"] * 0.2  # 起始纵坐标
        y2 = window["height"] * 0.8  # 终止纵坐标
        self.driver.swipe(x, y1, x, y2)

    def swipeToLeft(self):
        window = self.driver.get_window_size()
        x1 = window["width"] *0.8 #起始横坐标
        x2 = window["width"] *0.2 #终止横坐标
        y = window["height"] *0.5 #保持纵坐标不变
        self.driver.swipe(x1,y,x2,y)

    def swipeToRight(self):
        window = self.driver.get_window_size()
        x1 = window["width"] *0.2 #起始横坐标
        x2 = window["width"] *0.8 #终止横坐标
        y = window["height"] *0.5 #保持纵坐标不变
        self.driver.swipe(x1,y,x2,y)
