# _*_ coding:utf-8 _*_
# @Time :2020/6/7 23:00
# @Author :yanxia
a="1234567890"
b="12"
f="34"
g="56"
c=[]
q=[]
w=[]
if b in a:
    c.append(b)
    if f in a.strip(b):
        q.append(f)
        if g in a.strip(b).strip(f):
            w.append(g)
            k= a.strip(b).strip(f).strip(g)
        elif g =="null":
            w.append("null")
    elif f == "null":
        q.append("null")
elif b == "null":
    c.append("null")


print(k)