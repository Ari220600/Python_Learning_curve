"""
Iterable - __iter__() or __getitem__()
Iterator - __next__()
Iteration -

"""

# def gen(n):
#     for i in range(n):
#         yield i

# g = gen(3)
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())


# for i in g:
#     print(i)

# h = 546546
# ier = iter(h)
# print(ier.__next__())
# print(ier.__next__())
# print(ier.__next__())
# for c in h:
#     print(c)


#Fivonacci


# def fib(n):
#     for i in range(n):
#         if i==0:
#             j=0
#             yield j
#         elif i==1:
#             k=1
#             yield k
#         else:
#             sum= j + k
#             j=k
#             k=sum
#             yield sum
#
# f=fib(10)
# for x in range(10):
#     print(f.__next__())



#Factorial


# import math
#
#
# def factorial(n):
#     for i in range(1,n+1):
#         yield math.factorial(i)
#
#
# f = factorial(10)
# for x in range(9):
#     print(f.__next__())