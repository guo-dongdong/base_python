#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @CreateTime    : 2020-06-10 17:00
# @Author  : guoDD
# @Email   : Email
# @File    : testdd

"""
	# 总金额100w，
	月利率0.003959，
	还7月。
	等额本金
	计算公式

"""

# zongjine = 1000000
# lilv = 0.003959
# yuefen = 7
# yue = int(input("输入第几个月"))
#
# benjin = zongjine/yuefen
# yuelixi = (zongjine-((yue-1)*1000))*lilv
#
# meiyuehuanzonge = benjin+yuelixi
# print(meiyuehuanzonge)
#
# # loan_amount = int(input("输入总贷款金额："))
# # Total_repayment_month = int(input("输入总还款月份："))
# # Monthly_interest = 0.003959
# # yue = int(input("输入还款月份（第几个月）："))


# def mon(p,n,r):
#     b=p*r*pow((1+r),n)/(pow((1+r),n)-1)
#     print(b)
#     d=p/n
#     for m in range(1,8):
#         print(m)
#           # (贷款金额-贷款金额/总月*（当前月）)
#         f=(p-d*(m-1))*r
#         g=(f+d)
#         print("第%s个月应还款%.2f"%(m,g))
# mon(1000000,7,0.003959)


def duplicate_removal(a):
    a_1 = []
    for i in a:
        if i in a_1:
            a_1.remove(i)
        else:
            a_1.append(i)
    return "".join(a_1)
print(duplicate_removal("xyyxzc"))