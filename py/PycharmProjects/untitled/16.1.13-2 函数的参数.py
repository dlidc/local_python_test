#usr/bin/env python3

# x的n次方 实现如下
x = float(input('x:'))
n = float(input('n:'))

# x = input('x',x)
# n= input('n',n)

def power(x, n):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s

print(int(power(x,n)))


#默认函数实现改版,默认求平方结果
x = float(input('x:'))
# n = float(input('n:'))

# x = input('x',x)
# n= input('n',n)

def power(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s

print(int(power(x,n=2)))


def enroll(name, gender, age=6, city='Beijing'):
    print('name:', name)
    print('gender:', gender)
    print('age:', age)
    print('city:', city)



def q1(first, second, third, *var, **dict):
    print('first=',first, 'second=',second, 'third=',third, 'var=',var, 'dict=',dict)

def q2(first, second, s= 1, *, coupe, **dict):
    print('first=',first, 'second=',second, 's=',s, 'coupe=',coupe ,'dict=',dict)
