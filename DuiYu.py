#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @CreateTime    : 2020-06-10 16:51
# @Author  : guoDD
# @Email   : Email
# @File    : DuiYu

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
desired_caps['appPackage'] = 'com.changhong.duiyu'
desired_caps['appActivity'] = 'com.duiyu.ui.splash.SplashActivity'
desired_caps['noReset'] = True     #不重置应用数据
desired_caps['fastReset'] = "false"
desired_caps['fullReset'] = "false"
desired_caps['chromeOptions'] = {
                'androidProcess': 'com.changhong.duiyu'
                }

#appium连接ip端口一致
#打开微信
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
driver.implicitly_wait(10)
# driver.find_element_by_xpath("//*[@text='同意']").click()
# sleep(4)
driver.find_element_by_xpath("//*[@text='我的']").click()
sleep(1)
driver.find_element_by_xpath("//*[@text='点击登录/注册']").click()
sleep(2)
driver.find_element_by_xpath("//*[@text='手机号']").send_keys("18298461920")
driver.find_element_by_xpath("//*[@text='密码']").send_keys("gd1993")
sleep(1)
driver.find_element_by_xpath("//*[@text='登录']").click()
sleep(2)
# 截图
driver.get_screenshot_as_file("test_Duiyu.png")
# 当前页面上的所有webview
cts = driver.contexts
print(cts)
# 切换webview
# sleep(4)
# driver.switch_to.context("WEBVIEW_com.tencent.mm:tools")
#打印当前页面的resource
# print(driver.page_source)



sleep(10)
driver.quit()

