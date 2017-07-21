#!/usr/bin/env python3
# # -*- coding: utf-8 -*-

# 啊 = {'nice':99}
# print(啊['nice'])
#
# 啊['nice'] = 50
# print(啊['nice'])
#
# 'nice' in 啊


# a = 'abc'
# a = a.replace('a', 'A')
# print(a)
#
# dict = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
# print(dict['Michael'])
#
# s1 = set([1, 1, 2, 2, 3, 3])
# print(s1)
# s2 = set([2, 3, 4])
# print(s1 & s2)
# print(s1 | s2)
#
# d = {
#     'Michael': 95,
#     'Bob': 75,
#     'Tracy': 85
# }
# print('d[\'Michael\'] =', d['Michael'])
# print('d[\'Bob\'] =', d['Bob'])
# print('d[\'Tracy\'] =', d['Tracy'])
# print('d.get(\'Thomas\', -1) =', d.get('Thomas', -1))


r1 = (1,2,3)
r2 = (1,[2,3])
d1 = {'c1':20}
d2 = {'c2':15}
d1['c1'] = r1
d2['c2'] = r2
print(d1)
print(d2)

s1 = set(r1)
# s2 = set(r2)
print(s1)
# print(s2)