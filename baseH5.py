#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @CreateTime    : 2020-06-02 10:07
# @Author  : guoDD
# @Email   : Email
# @File    : baseH5

"""
	
"""
from appium import webdriver
from time import sleep

# #手机版本要跟需要驱动的手机一致
# desired_caps = {}
# desired_caps['platformName'] = 'Android'
# desired_caps['platformVersion'] = '5.1.1'
# desired_caps['deviceName'] = 'poo'
#
# #app具体配置与实际抓出来的一致
# # com.changhong.duiyu/com.duiyu.ui.splash.SplashActivity
# # com.android.browser/.BrowserActivity
# desired_caps['appPackage'] = 'com.android.browser'
# desired_caps['appActivity'] = '.BrowserActivity'
#
# desired_caps['noReset'] = True     #不重置应用数据
# desired_caps['noSign'] = True     #不重新签名APP
# desired_caps['unicodeKeyboard'] = True     #支持中文输入
# desired_caps['resetKeyboard'] = True     #重置输入法为系统默认
#
# #打开APP
# driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
from baseDriver import appium_H5_driver

device = {
    'platformName' : 'Android',
    'platformVersion' : '5.1',
    'deviceName' : 'huawei',
    'appPackage' : 'com.android.browser',
    'appActivity' : '.BrowserActivity',
    'port' : '4723'
}

driver = appium_H5_driver(device)
driver.implicitly_wait(10)
sleep(2)
#打开豆瓣首页
driver.get("https://m.douban.com")
#点击进入网页版
driver.find_element_by_xpath('//*[@text="进入网页版 >"]').click()
sleep(2)
# 找电影 影院热映
driver.find_element_by_xpath('//*[@text="找电影 影院热映"]').click()
sleep(2)





sleep(10)
driver.quit()