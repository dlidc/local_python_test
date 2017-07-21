#!usr/bin/env python3
# -*- coding:utf-8 -*-   or  # coding=utf-8
L = ['leonard','shelton','penny','howard','raj' ]
L[0:3]
print(L)
print(L[0:3])   #从0到3 不包括3; 0 1 2


#第一个索引是0 甚至可以这么做
print(L[:4])

#倒数的切片
print(L[:-2])
print(L[-2:-1])

print(L[-2:0])
print(L[-3:-1])
print(L[-3:0])
print(L[-3:-4])
print(L[-4:-3])

print(L[-3:-1])
#倒数第一索引是 -1  方向是从左往右  ########左闭右开
###记住倒数第一个元素的索引是-1。


# 前十个 L[:10]
# 后十个 L[-10:]
# 前11-20个数：  L[10:20]
# 前10-20个数:   L[9:20]
#
# 前10个数，每两个取一个：
#
# >>> L[:10:2]
# [0, 2, 4, 6, 8]
#
# 所有数，每5个取一个：
#
# >>> L[::5]
# [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95]
#
# 甚至什么都不写，只写[:]就可以原样复制一个list：
#
# >>> L[:]
# [0, 1, 2, 3, ..., 99]

#
# tuple  元组切片方法
# T =  tuple(range(100))
# T[:10:5]
# 或者  (1,2,2,3,4,5,6)[::2]
#
# 表和元组可以切片
# 集合set 并不能

#字符串也能切，原理是字符串可以看为为数字组合起来的表（list）
#'1234567890qwertyuiop'[::5]

##############能切的 list tuple str ############