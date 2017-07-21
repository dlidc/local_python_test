#!/usr/bin/python
# -*- coding: UTF-8 -*-


#>>> [x * x for x in range(1, 11)]
#[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# >>> [x * x for x in range(1, 11) if x % 2 == 0]
# [4, 16, 36, 64, 100]

# >>> d = {'x': 'A', 'y': 'B', 'z': 'C' }
# >>> for k, v in d.items():
# ...     print(k, '=', v)


##注意：此循环中 k,v 仅为规范选择，实际可自定义

# L = ['Hello', 'World', 18, 'Apple', None]
# [s.lower(for s in L)]
# if isinstance(x, str):
#     print(s.lower)


L1 = ['Hello','world',18,'Apple',None]
L2 = [s.lower() for s in L1 if isinstance(s,str)]
print(L2)