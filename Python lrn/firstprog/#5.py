# Exercise 4
# Pattern Printing
# Input = Integer n
# Boolean = True or False
#
# True n=5
# *
# **
# ***
# ****
#
# False n=5
# ****
# ***
# **
# *
def fun():
    a=int(input("The numbers of rows:\n"))
    b=bool(int(input("press 1 to print low to high\npress 0 to print high to low\n")))
    if b==True:
        for i in range(0,a+1):
            print("*"*int(i))
    else:
        for i in range(a,0,-1):
            print("*"*int(i))
fun()
while 1:
    x=bool(int(input("press 1 to try again\npress 0 to stop\n")))
    if x==True:
        fun()
    else:
        print("\t\t! ! ! Thank You ! ! !")
        break