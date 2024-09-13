#A simple adding program
#BUT the more you use the program the more it will take time to process
#unless you have opened it 5 times then it will reset it automatically

import time
with open("#8timect.txt","r+") as f:
    while 1:
        try:
            a=int(input("enter your first number\n"))
            b=int(input("enter your second number\n"))
            break
        except:
            print("FOR GOD'S SAKE\nEnter a valid number or fuck yourself\n")
    x=len(f.readlines())
    if x>=5:
        f.seek(0)
        f.truncate()
        print(f"please wait for 5 seconds")
        time.sleep(5)
    else:
        print(f"please wait for {x} seconds")
        time.sleep(x)
        time.sleep(x)
        f.write("line\n")

    print("the sum is : ",a+b)