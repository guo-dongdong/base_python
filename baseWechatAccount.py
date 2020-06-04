#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @CreateTime    : 2020-06-02 14:02
# @Author  : guoDD
# @Email   : Email
# @File    : baseWechatAccount

"""
	
"""

from baseDriver import appium_wechatAccount_driver
from time import sleep
from appium import webdriver

device = {
    'platformName' : 'Android',
    'platformVersion' : '5.1',
    'deviceName' : 'huawei',
    'port' : '4723'
}

driver = appium_wechatAccount_driver(device)
driver.implicitly_wait(10)
sleep(9)

driver.find_element_by_xpath("//*[@text='通讯录']").click()
sleep(5)
driver.find_element_by_xpath("//*[@text='公众号']").click()
sleep(5)
driver.find_element_by_xpath("//*[@text='爱心筹']").click()
sleep(5)
driver.find_element_by_xpath("//*[@text='我的筹款']").click()
sleep(5)
driver.find_element_by_xpath("//*[contains(@text,'我要提现')]").click()
sleep(5)
#当前页面上的所有view

cts = driver.contexts

print(cts)
#进行webview的切换
driver.switch_to.context('WEBVIEW_com.tencent.mm:tools')

#打印当前页面的resource
print(driver.page_source)
#选择提现
driver.find_element_by_partial_link_text("提现").click()
sleep(2)
driver.find_element_by_link_text("去添加").click()
sleep(2)
driver.switch_to.context('NATIVE_APP')
driver.quit()
