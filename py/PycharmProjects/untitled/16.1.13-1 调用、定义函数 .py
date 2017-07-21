#usr/bin/env python3
def your_abs(a):
    if a == 1:
        return a
    else:
        return -a

#空函数
def nop():
    pass
#pass=占位符


#不知道怎么写 先放个pass，使程序能够正常运行

x = 0
def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x

print(my_abs(x))


import math

def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny

x, y = move(100, 100, 60, math.pi / 4)
print(x, y)

r = move(100, 100, 60, math.pi / 6)
print(r)


#****以下是
#ax2 + bx + c = 0 接受abc三个值，返回一元二次方程的code

import math
a = float(input('please input a = '))
b = float(input('please input b = '))
c = float(input('please input c = '))

def quadratic(a, b, c):
    if not isinstance (a, (int, float)):
        raise TypeError ('error a的数据类型')
    if not isinstance (b, (int, float)):
        raise TypeError ('error b的数据类型')
    if not isinstance (c, (int, float)):
        raise TypeError ('error c的数据类型')


def quadratic(a, b, c):
#ax2 + bx + c = 0
    team = b*b-4*a*c
    if a  == 0:
        x1 = -c/b
        return x1
    elif team > 0:
        x1 = (-b+math.sqrt(team))/(2*a)
        x2 = (-b-math.sqrt(team))/(2*a)
        return x1,x2
    elif team < 0:
        x1 = -b/(2*a)
        return x1
    else:
        print(无实数解)
print(quadratic(a,b,c))

