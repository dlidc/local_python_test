#!/usr/bin/python
# -*- coding: UTF-8 -*-

# age = int(input('小妹妹你几岁啦:'))
# if age <= 12:
#     print('萝莉')
# elif age <= 18:
#     print('学生妹')
# elif age >= 25:
#     print('姐姐')
# else :
#     print('少女')


# birth = int(input('birth: '))
# if birth < 2000:
#     print('00前')
# else:
#     print('00后')

height = float(input('请输入你的体重，单位公斤谢谢：'))
long = float(input('请输入你的身高，单位米谢谢：'))

bmi = (height/(long*long))
print('您的bmi指数是,%f'%bmi)

if bmi < 18.5:
    print('过轻')
elif bmi < 25:
    print('正常')
elif bmi < 28:
    print('肥胖')
elif bmi < 32:
    print('肥胖')
else:
    print('严重肥胖')