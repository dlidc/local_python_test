#!/usr/bin/env python3
# -*- coding: utf-8 -*-





#
#
# class human(object):
#     def a(self):
#         print('this is first default method')
#
#
# goodman = human()
# badman = human()
# print goodman
# print badman
#
# goodman.a()
# badman.a()
#
# goodman.life = 'bright'
# badman.life = 'bored'
#
# print goodman.__dict__
#
# goodman.__class__.one = 1
# print goodman.__class__.__dict__
#
#
# class Student():
#     def __init__(self, name, score):
#         self.name = name
#         self.score= score
#     def print_score(self):
#         print('%s: %s' % (self.name, self.score))
#
# bart = Student('baba', 90)
# print bart.name
# print bart.score
# print bart
# print Student.print_score(bart)
#
#
#
#
#
#
#
#
#
# a = 'xyz'
# print a
# b = a
# print b
# a = 'abc'
# print b
# print a
#




#
# class Student:
#     pass
# bart =Student()
# print(bart)



#tuple

# L = [
#     ['Apple', 'Google', 'Microsoft'],
#     ['Java', 'Python', 'Ruby', 'PHP'],
#     ['Adam', 'Bart', 'Lisa']
# ]
#
# #打印Apple:
# print(L[0][0])
# #打印Python:
# print(L[1][1])
# #打印Lisa:
# print(L[2][2])
#
# print('%s\n%s\n%s\n' % (L[0][0],L[1][1],L[2][2]))


# age = 20
# if age >= 17:
#     print ('big')
#     else


# age = input('age:')
# if age >= 20 :
#      print('adult')
# elif age <10 :
#      print('child')
# else:
#      print('二次元')


###BMI = 體重(公斤) / 身高2(公尺2)

Weight = input('体重kg:')
Height = input('身高m:')  #需要限制 否则失误 或者加自动转换的
BMI = Weight/(Height**2)
print('BMI指数是: %f' % BMI)
if BMI < 18.5:
    print('过轻')
elif BMI < 25:
    print('正常')
elif BMI < 28:
    print ('过重')
elif BMI < 32:
    print ('肥胖')
elif BMI < 999:
    print ('monster')



