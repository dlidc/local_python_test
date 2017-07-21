#usr/bin/env python3

n = float(input('input:'))


def fact(n):
    if n==1:
        return 1
    return n * fact(n - 1)
print(fact(n))


#并不是优化的优化 逻辑很诡异
def fact(n):
    return fact_iter(n, 1)

def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)
#*****计算过程***** fact_iter(n-1,n*product) -->fact_iter(n-2,(n-1)*(n*product))
#    |  (n-1,n*product)  |   (n-2,(n-1)*'n*product')  | (n-3,(n-2)'(n-1)*n*product')


def move(n,a,b,c):
    if n == 1:
        print(a,'-->',c)
        return
    move(n-1,a,c,b)
    move(1,a,b,c)     #也可作print(a,'-->',c)
    move(n-1,b,a,c)

move(5,"a","b","c",)
# #代码：
# def mov(n,a,b,c):
#     if 1==n:
#         print(a,'-->',c)    #如果只有一个盘子，直接从A动到C
#     else:
#         mov(n-1,a,c,b)    #step1：将前n-1个盘子从A移动到B
#         mov(1,a,b,c)    #step2：将最底下的第n号盘子从A移动到C
#         mov(n-1,b,a,c)    #step3：将B上的n-1个盘子移动到C
#
# #递归过程分解，n>3时同理：
# mov(3,A,B,C)    #调用函数
#     mov(2,A,C,B)        #step1：将前n-1个盘子从A移动到B
#         mov(1,A,B,C)    #打印A-->C
#         mov(1,A,C,B)    #打印A-->B
#         mov(1,C,A,B)    #打印C-->B
#
#                         #step2：将最底下的第n号盘子从A移动到C
#     mov(1,A,B,C)        #打印A-->C
#
#     mov(2,B,A,C)        #step3：将B上的n-1个盘子移动到C
#         mov(1,B,C,A)     #打印B-->A
#         mov(1,B,A,C)     #打印B-->C
#         mov(1,A,B,C)     #打印A-->C