#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @CreateTime    : 2020-05-22 13:42
# @Author  : guoDD
# @Email   : Email
# @File    : testStu

"""
	
"""
# 冒泡排序
# def bubbleSort(a):
#     for i in range(len(a) -1):
#         for j in range(len(a) -i -1):
#             if a[j] > a[j+1]:
#                 a[j],a[j+1] = a[j+1],a[j]
#     return a

a = [9, 2, 4, 5, 7, 9, 0, 1, 5,10,20,19,34,8]

# print(bubbleSort(a))

# # 列表结尾添加单独元素
# a.append(11)
#
# # 列表结尾添加另一个列表的元素
# l = [99,88]
# a.extend(l)

# # 指定位置添加元素insert(下标，元素)
# a.insert(0,100)

# # 删除元素  删除列表中值为 x 的第一个元素。如果没有这样的元素，就会返回一个错误。
# # a.remove(9)
# #
# # # 从列表的指定位置移除元素，并将其返回
# # a.pop(0)

# # 移除列表中的所有项
# a.clear()

# # 返回列表中第一个值为 x 的元素的索引。如果没有匹配的元素就会返回一个错误。
# print(a.index(9))
#
# # 返回 x 在列表中出现的次数。
# print(a.count(9))

# # 对列表中的元素进行排序。
# a.sort()
# # 倒序
# a.reverse()

# 列表的浅复制
print(a.copy())
print(a)