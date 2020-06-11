#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @CreateTime    : 2020-06-10 14:03
# @Author  : guoDD
# @Email   : Email
# @File    : weChatGZH

"""
	
"""
from appium import webdriver
from time import sleep


#手机版本要跟需要驱动的手机一致
desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '8'
desired_caps['deviceName'] = 'XIAOMI6_DINGZIHU'

#app具体配置与实际抓出来的一致
# com.changhong.duiyu/com.duiyu.ui.splash.SplashActivity
'''
通过cmd命令，前提是先打开手机中你要获取包名的APP
1. adb shell
2. dumpsys activity | grep mFocusedActivity
'''
'''
adb shell dumpsys window | findstr mCurrentFocus
'''

# com.android.browser/.BrowserActivity
# com.tencent.mm/com.tencent.mm.ui.LauncherUI
desired_caps['appPackage'] = 'com.tencent.mm'
desired_caps['appActivity'] = 'com.tencent.mm.ui.LauncherUI'
desired_caps['noReset'] = True     #不重置应用数据
desired_caps['fastReset'] = "false"
desired_caps['fullReset'] = "false"
desired_caps['chromeOptions'] = {
                'androidProcess': 'com.tencent.mm:tools'
                }

#appium连接ip端口一致
#打开微信
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
driver.implicitly_wait(10)
sleep(7)

# 进入公众号
driver.find_element_by_xpath("//*[@text='通讯录']").click()
sleep(2)
driver.find_element_by_xpath("//*[@text='公众号']").click()
sleep(2)
driver.find_element_by_xpath("//*[@text='爱心筹']").click()
sleep(2)
driver.find_element_by_xpath("//*[@text='我的筹款']").click()
sleep(2)
driver.find_element_by_xpath("//*[contains(@text,'我要提现')]").click()
sleep(5)
driver.get_screenshot_as_file("test.png")
# 当前页面上的所有webview
cts = driver.contexts
print(cts)
# 切换webview
sleep(4)
driver.switch_to.context("WEBVIEW_com.tencent.mm:tools")
#打印当前页面的resource
print(driver.page_source)



sleep(10)
driver.quit()