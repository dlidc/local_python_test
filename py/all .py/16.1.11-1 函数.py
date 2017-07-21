#!/usr/bin/env python3


##调用函数


n1 = 255
n2 = 65535
print(hex(n1))
print(hex(n2))

##定义函数


x = -5
def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x
print(my_abs(x))

