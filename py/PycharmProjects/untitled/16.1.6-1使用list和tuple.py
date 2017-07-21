#!/usr/bin/python
# -*- coding: UTF-8 -*-

# list


room1 = ['101','102','103','104']
print(room1)

room = ["101","102","103","104"]
print(room)

# the same

a1 = 1
a2 = 2
a3 = 3
a4 = 4
a5 = 5
home = [a1,a2,a3,a4,a5]
print(home)


print(len(home))
print(len(room))

#按照索引位置
print(room[1])
print(room[0])
#倒叙索引，-1=最后一个，-2倒数第二个
print(room[-1])
print(room[-2])

room.append('909')
room.insert(1,'303')
print(room)

flash = ('lee','yong','hoo')
#tuple（元祖），初始化后不能修改，你可以正常地使用classmates[0]，classmates[-1]，但不能赋值成另外的元素。
print(flash)

classmates = ('Michael', 'Bob', 'Tracy')
print(classmates)

# 定义的不是tuple，是1这个数！这是因为括号()既可以表示tuple，又可以表示数学公式中的小括号，这就产生了歧义，因此，Python规定，这种情况下，按小括号进行计算，计算结果自然是1。
#
# 所以，只有1个元素的tuple定义时必须加一个逗号,，来消除歧义：
qqq = (1,)
print(qqq)

qq = ()
print(qq)

t = ('a', 'b', ['A', 'B'])
t[2][0] = 'X'   #第三序列中第一序列 变量为x
t[2][1] = 'Y'   #第三序列中第二序列 变量为y
print(t)


# -*- coding: utf-8 -*-

L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]

print('# 打印Apple:',L[0][0])
print('# 打印Python:',L[1][1])
print('# 打印Lisa:',L[2][2])