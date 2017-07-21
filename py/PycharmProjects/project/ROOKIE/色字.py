import random

print ('game start')
# choice = ('big/small')
choice = input('input your choice: big/small')


p1 = random.randrange(1,7)
p2 = random.randrange(1,7)
p3 = random.randrange(1,7)

value =  p1 + p2 + p3

isBig = 11 <=  value
isSmall = value <=10

if value >= 11:
    print('da',value,p1,p2,p3 )
else:
    print('xiao',value, p1, p2, p3)

