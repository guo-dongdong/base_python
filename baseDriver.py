#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @CreateTime    : 2020-06-02 10:39
# @Author  : guoDD
# @Email   : Email
# @File    : baseDriver

"""
	
"""
from appium import webdriver

# driver封装
# app
def appium_driver(device):
    desired_caps = {}
    desired_caps['platformName'] = device['platformName']
    desired_caps['platformVersion'] = device['platformVersion']
    desired_caps['deviceName'] = device['deviceName']

    desired_caps['appPackage'] = device['appPackage']
    desired_caps['appActivity'] = device['appActivity']

    #打开APP
    driver = webdriver.Remote('http://localhost:'+device['port']+'/wd/hub', desired_caps)
    return driver

# 微信小程序
def appium_wechatapplet_driver(device):
    desired_caps = {}
    desired_caps['platformName'] = device['platformName']
    desired_caps['platformVersion'] = device['platformVersion']
    desired_caps['deviceName'] = device['deviceName']
    # app具体配置与实际抓出来的一致
    desired_caps['appPackage'] = 'com.tencent.mm'
    desired_caps['appActivity'] = 'com.tencent.mm.ui.LauncherUI'
    desired_caps['noReset'] = True  # 不重置应用数据
    desired_caps['fastReset'] = 'false'
    desired_caps['fullReset'] = 'false'
    desired_caps['chromeOptions'] = {
        'androidProcess': 'com.tencent.mm:appbrand0'
    }

    # appium连接ip端口一致
    # 打开APP
    driver = webdriver.Remote('http://localhost:' + device['port'] + '/wd/hub', desired_caps)
    return driver

# 微信公众号
def appium_wechatAccount_driver(device):
    desired_caps = {}
    desired_caps['platformName'] = device['platformName']
    desired_caps['platformVersion'] = device['platformVersion']
    desired_caps['deviceName'] = device['deviceName']
    # app具体配置与实际抓出来的一致
    # com.tencent.mm/com.tencent.mm.ui.LauncherUI
    desired_caps['appPackage'] = 'com.tencent.mm'
    desired_caps['appActivity'] = 'com.tencent.mm.ui.LauncherUI'
    desired_caps['noReset'] = True  # 不重置应用数据
    desired_caps['fastReset'] = 'false'
    desired_caps['fullReset'] = 'false'
    desired_caps['chromeOptions'] = {
        'androidProcess': 'com.tencent.mm:tools'
    }

    # appium连接ip端口一致
    # 打开微信
    driver = webdriver.Remote('http://localhost:' + device['port'] + '/wd/hub', desired_caps)
    return driver

# H5
def appium_H5_driver(device):
    desired_caps = {}
    desired_caps['platformName'] = device['platformName']
    desired_caps['platformVersion'] = device['platformVersion']
    desired_caps['deviceName'] = device['deviceName']

    desired_caps['appPackage'] = device['appPackage']
    desired_caps['appActivity'] = device['appActivity']

    desired_caps['noReset'] = True  # 不重置应用数据
    desired_caps['noSign'] = True  # 不重新签名APP
    desired_caps['unicodeKeyboard'] = True  # 支持中文输入
    desired_caps['resetKeyboard'] = True  # 重置输入法为系统默认

    # 打开APP
    driver = webdriver.Remote('http://localhost:'+device['port']+'/wd/hub', desired_caps)
    return driver