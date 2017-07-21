#！usr/bin/env python3



#######迭代字典key
d = {'a': 1, 'b': 2, 'c': 3}
for key in d:
    print(key)


#######迭代字典value
for value in d.values():
    print(value)

#######迭代字典key和value

for k, v in d.items():
    print(k,v)


##字符串也可以迭代

for ch in 'abc':
    print(ch)






from collections import Iterable
isinstance('abc',Iterable)

>>> for i, value in enumerate(['A', 'B', 'C', 'S', 'R']):
...     print(i,value)