#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @CreateTime    : 2020-05-29 9:28
# @Author  : guoDD
# @Email   : Email
# @File    : appiumWeChat



from appium import webdriver
from time import sleep


#手机版本要跟需要驱动的手机一致
desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '9'
desired_caps['deviceName'] = 'XiaoMi8'

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
window = driver.get_window_size()
x = window["width"] * 0.5       #横轴不变
y1 = window["height"] * 0.2     #起始纵轴
y2 = window["height"] * 0.8     #结束纵轴

driver.swipe(x,y1,x,y2)
print("滑动完成")


sleep(10)
driver.quit()