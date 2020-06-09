#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @CreateTime    : 2020-06-08 10:04
# @Author  : guoDD
# @Email   : Email
# @File    : testCar

import re

line = ["回复：【项目上线】卡家实验室bug修复上线",
        "回复：【项目上线】卡家实验室迭代",
        "回复：【项目上线】卡家实验室迭代",
        "回复：【项目上线】经销商-卡商宝-双呼状态修复-v2.1.15",
        "回复：【项目上线】App极速版-司机招聘-v1.2.4-修复百度接口更换导致无法上传驾照问题",
        "回复：【项目上线】产品库-后台v1.0-图片查询",
        "回复：【项目&数据库更新上线】产品库v1.1.0_配件查询后台二期 & Truckhome_v1.1.0_新增发动机关联表及滤芯关联表",
        "回复：【数据库上线】TruckTopic_1.0.0_柳汽乘龙百万运营官 新建数据表",
        "回复：【项目上线】产品库-询价短信下线_V1.0.1"
        ]

# 产品
product_list = ["卡家实验室","互动","经销商","bbs","APP","产品库","TruckTopic","资讯","商业配合","DB","其他","APP项目",
                "电商","公共服务","App极速版","智慧站长","ApiSearch","解放轻卡","独立","IT系统","青汽车联网","互助军团","云卡",
                "结算系统"]
business_list = ["后台","卡商宝","司机招聘","询价短信下线"]
version_list = []
listPro=[]
listBus=[]
version=[]
remarks=[]


for email_Subject in line:
    # 提取产品
    for i in product_list:
        # 判断产品线列表中的值是否在邮件主题中，有的话，插入到listPro=[]里，并结束循环
        if i in email_Subject:
            listPro.append(i)
            break
    # 判断如果所有产品线列表中的值都没有在邮件主题中出现，那就把null插入到插入到listPro[]
    if i not in email_Subject:
        listPro.append("null")

    # 提取业务线（逻辑和提取产品线一样）
    for j in business_list:
        # 判断产品线列表中的值是否在邮件主题（邮件主题中删除了产品线）中，有的话，插入到listBus=[]里，并结束循环
        if j in email_Subject.replace(i, ""):
            listBus.append(j)
            break

    # 判断如果所有业务线列表中的值都没有在邮件主题中出现，那就把null插入到插入到listBus[]
    if j not in email_Subject.replace(i, ""):
        listBus.append("null")

    # 版本号
    v = re.findall(r'\d+\.(?:\d+\.)*\d+', email_Subject.replace(i, "").replace(j, ""))
    ver = ''.join(v)
    # 如果没有找到版本号，就version=[]中插入null；否则插入ver
    if ver == "":
        version.append("null")
    else:
        version.append(ver)

    # 邮件标题中，删除产品、业务、版本号。再删除其他一些没用的信息，其他的就是备注
    remarks.append(email_Subject.replace(i, "").replace(j, "").replace(ver, "").replace("回复：", "").replace("【项目上线】", "")
                   .replace("-", "").replace("_", "").replace("【数据库上线】", "").replace("v", "").replace("V", ""))

print(listPro)
print(listBus)
print(version)
print(remarks)
print(len(listPro))
print(len(listBus))
print(len(version))
print(len(remarks))