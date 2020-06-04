#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @CreateTime    : 2020-05-28 11:19
# @Author  : guoDD
# @Email   : Email
# @File    : testappium

# from appium import webdriver
from time import sleep
from baseDriver import appium_driver, appium_wechatapplet_driver

# #手机版本要跟需要驱动的手机一致
# desired_caps = {}
# desired_caps['platformName'] = 'Android'
# desired_caps['platformVersion'] = '9'
# desired_caps['deviceName'] = 'HUAWEI'
#
# #app具体配置与实际抓出来的一致
# # com.changhong.duiyu/com.duiyu.ui.splash.SplashActivity
# # com.android.browser/.BrowserActivity
# desired_caps['appPackage'] = 'com.changhong.duiyu'
# desired_caps['appActivity'] = 'com.duiyu.ui.splash.SplashActivity'

# device = {
#     'platformName' : 'Android',
#     'platformVersion' : '5.1',
#     'deviceName' : 'huawei',
#     'appPackage' : 'com.changhong.duiyu',
#     'appActivity' : 'com.duiyu.ui.splash.SplashActivity',
#     'port' : '4723'
# }
# print(device)
# print(type(device))
#
# # #appium连接ip端口一致
# # #打开兑鱼
# # driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
#
# driver = appium_driver(device)
#
# driver.implicitly_wait(10)
#
#
# # # 点击同意协议
# # driver.find_element_by_id("com.changhong.duiyu:id/btn_confirm").click()

# 调微信小程序
device = {
    'platformName' : 'Android',
    'platformVersion' : '5.1',
    'deviceName' : 'huawei',
    'port' : '4723'
}
driver = appium_wechatapplet_driver(device)
driver.implicitly_wait(10)

sleep(9)
#对微信操作
#打开发现
driver.find_element_by_android_uiautomator('new UiSelector().text("发现")').click()
sleep(2)
#打开朋友圈
driver.find_element_by_xpath("//*[@text='朋友圈']").click()
sleep(2)
#返回
driver.find_element_by_id("com.tencent.mm:id/m0").click()
# driver.find_element_by_id("com.tencent.mm:id/lz").click()
sleep(2)
#点击微信
driver.find_element_by_android_uiautomator('new UiSelector().text("微信")').click()
sleep(3)


sleep(10)
driver.quit()