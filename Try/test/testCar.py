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


# def Extract_value(i_list,j_list,fill_list):
#     for i in i_list:
#         for j in j_list:
#             if i in j:
#                 fill_list.append(i)
#                 j = j.strip(i)
#             else:
#                 fill_list.append("null")
#     return  i_list,j_list,fill_list
#
#
# Extract_value(product_list,line,listPro)
#
# # Extract_value(business_list,line,listBus)
for x in line:
    ver = re.findall(r'\d+\.(?:\d+\.)*\d+',x)
    version_list.append(ver)
# print(version_list)


for i in product_list:
    for j in line:
        if i in j:
            listPro.append(i)
            for n in business_list:
                if n in j.strip(i):
                    listBus.append(n)
                    for v in version_list:
                        if str(v) in j.strip(i).strip(n) and len(v)>0:
                            version.append(v)
                            k = j.strip(i).strip(n).strip(v)
                            # remarks.append(k)
                            print(k)
                            product_list.remove(j)



print(listPro)
print(listBus)

print(remarks)
