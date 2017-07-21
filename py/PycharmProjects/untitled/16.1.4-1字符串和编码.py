# print('您的余额已经不足，请及时充值')
#
# money = input('充值金额:')
# sq = '您的余额是:{money}'
# sq.format(money)
# print(sq)
#
#

a = 'ibm is a great %s'%'company'
print(a)

b = 'microsoft has %d dollars %s , however ,it\'s %f of apple.inc'%(1000,'in nasdaq today',0.65)
print(b)
#在字符串中赋值
#但是怎么做到 %d ,%s,%f,%x  可变

i = 'abc what is likely 0x such as %x'% 160
ig = 'abc what is likely 0x such as %x'% 0x321
print(i)
print(ig)

# i = 'abc what is likely 0x such as %x'% 160  这里面的 %后数字转换成十六进制

#转义#
igs = 'apple.inc has a grownth of iphone increased by %% %d in 2013q4 '% 25
print(igs)


# # -*- coding: utf-8 -*-
# s1 = 72
# s2 = 85
# s3 = s2-s1
# print('''背景：小明和老师在办公室;
# 小明啊，我作为一个长者得跟你谈谈''')
# print('你去年成绩:%d ,今年成绩：%d' %(s1,s2))
# print('你的成绩提高了%d分 ,提高了%0.2f,也就是%d%%' % (s3,s3/s1,int(s3/s1*100)))
# print('''我今天是作为一个长者跟你们讲。我不是老师，但是我见得太多了。我有这个必要好告诉你们一点人生的经验
# 你啊，我感觉你啊还要学习一个。你们毕竟还too young.明白我的意思吧？
# 唉，我也替你着急啊。
# 好了好了，出去吧。
# 顺便把下一个同学叫进来。''')
# print('小明：吼啊,再见，老师.')
# asdddddddddddddddddddddddddddddddddd=input('Enter to continue;')
# print('同学叫什么名字;')
# name=('我叫：')
# print('你上次考试多少分啊|')
# date1=input('老师，我考了：')
# date1=int(date1)
# print('那你这次考多少分啊|')
# date2=input(':')
# date2=int(date2)
# x=date2-date1
# y=date1-date2
# if x > 0:
#     print('不错，继续努力。成绩提高了%0.1f%%' %(x/date1*100))
# elif x < 0:
#     print('干什么吃的，好好学。下降了%0.1f%%' %(y/date1*100))
# else:
#     print('学如逆水行舟，不尽则退，加吧劲吧')


# g1 = int(input("请输入您上次的成绩:"))
# g2 = int(input("请输入您本次的成绩:"))
# r = ((g2-g1)/g1)*100
# if r > 0:
#     print("恭喜,你的成绩比上次提高了%.2f%%!"%r)
# elif r == 0:
#     print("您的成绩没有改变.")
# elif r < 0:
#     print("您的成绩比上次下降了%.2f%%,请继续努力."%-r)

l1 = int(input("上次考试成绩:"))
l2 = int(input("下次保证考成绩:"))

re = ((l2-l1)/l1)*100

if re > 0:
    print("提高%.2f%%"%re)
elif re == 0:
    print("原地踏步")
elif re < 0:
    print("还不如原来,下降了%.2f%%"%-re)

# 此例不支持浮点数.比如0.5分
print('分别来处理""')
print("和''的问题，单引号和双引号都一样")

