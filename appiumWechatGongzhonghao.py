#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @CreateTime    : 2020-05-29 16:06
# @Author  : guoDD
# @Email   : Email
# @File    : appiumWechatGongzhonghao

"""
	
"""
from appium import webdriver
from time import sleep


#手机版本要跟需要驱动的手机一致
desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '8.0'
desired_caps['deviceName'] = 'XiaoMi6'

desired_caps['appPackage'] = 'com.tencent.mm'
desired_caps['appActivity'] = '.ui.LauncherUI'
desired_caps['noReset'] = True     #不重置应用数据
desired_caps['fastReset'] = "false"
desired_caps['fullReset'] = "false"
desired_caps['chromeOptions'] = {
                'androidProcess': 'com.tencent.mm:appbrand0'
                }

#appium连接ip端口一致
#打开微信
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
driver.implicitly_wait(10)
sleep(5)
#向下滑动微信



sleep(10)
driver.quit()