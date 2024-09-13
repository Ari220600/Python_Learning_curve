# Health Management System
# 3 clients - Harry, Rohan and Hammad



# Total 6 files
# write a function that when executed takes as input client name
# One more function to retrieve exercise or food for any client
def getdate():
    import datetime
    return datetime.datetime.now()


def datainput(x):
    if x==1:
        c=int(input("1: for food\n2: for exercise\n"))
        if c==1:
            value=input("Type here\n")
            with open("#Samrat_Food.txt","a") as op:
                op.write(str([str(getdate())])+":"+value+ "\n")
            print("Input Successfull\n")
        elif c==2:
            value=input("Type here\n")
            with open("#Samrat_Exercise.txt","a") as op:
                op.write(str([str(getdate())])+":"+value+ "\n")
            print("Input Successfull\n")
    elif x==2:
        c=int(input("1: for food\n2: for exercise\n"))
        if c==1:
            value=input("Type here\n")
            with open("#Sarthak_Food.txt","a") as op:
                op.write(str([str(getdate())])+":"+value+ "\n")
            print("Input Successfull\n")
        elif c==2:
            value=input("Type here\n")
            with open("#Sarthak_Exercise.txt","a") as op:
                op.write(str([str(getdate())])+":"+value+ "\n")
            print("Input Successfull\n")
    elif x==3:
        c=int(input("1: for food\n2: for exercise\n"))
        if c==1:
            value=input("Type here\n")
            with open("#Deep_Food.txt","a") as op:
                op.write(str([str(getdate())])+":"+value+ "\n")
            print("Input Successfull\n")
        elif c==2:
            value=input("Type here\n")
            with open("#Deep_Exercise.txt","a") as op:
                op.write(str([str(getdate())])+":"+value+ "\n")
            print("Input Successfull\n")
    if x==4:
        c=int(input("1: for food\n2: for exercise\n"))
        if c==1:
            value=input("Type here\n")
            with open("#Anik_Food.txt","a") as op:
                op.write(str([str(getdate())])+":"+value+ "\n")
            print("Input Successfull\n")
        elif c==2:
            value=input("Type here\n")
            with open("#Anik_Exercise.txt","a") as op:
                op.write(str([str(getdate())])+":"+value+ "\n")
            print("Input Successfull\n")
def retrieve(x):
    if x==1:
        c=int(input("1: for food\n2: for exercise\n"))
        if c==1:
            with open("#Samrat_Food.txt","rt") as ip:
                for i in ip:
                    print(i, end="")
        elif c==2:
            with open("#Samrat_Exercise.txt","rt") as ip:
                for i in ip:
                    print(i, end="")
    if x==2:
        c=int(input("1: for food\n2: for exercise\n"))
        if c==1:
            with open("#Sarthak_Food.txt","rt") as ip:
                for i in ip:
                    print(i, end="")
        elif c==2:
            with open("#Sarthak_Exercise.txt","rt") as ip:
                for i in ip:
                    print(i, end="")
    if x==3:
        c=int(input("1: for food\n2: for exercise\n"))
        if c==1:
            with open("#Deep_Food.txt","rt") as ip:
                for i in ip:
                    print(i, end="")
        elif c==2:
            with open("#Deep_Exercise.txt","rt") as ip:
                for i in ip:
                    print(i, end="")
    if x==4:
        c=int(input("1: for food\n2: for exercise\n"))
        if c==1:
            with open("#Anik_Food.txt","rt") as ip:
                for i in ip:
                    print(i, end="")
        elif c==2:
            with open("#Anik_Exercise.txt","rt") as ip:
                for i in ip:
                    print(i, end="")
while 1:
    j=int(input("1: Start\n2: Exit\n"))
    if j==1:
        x=int(input("1: for data retrieve\n2: for data input\n"))
        k=int(input("1: Samrat\n2: Sarthak\n3: Deep\n4: Anik\n"))
        if x==1:
            try:
                retrieve(k)
            except:
                print("Data unavailable")
                continue
        elif x==2:
            datainput(k)
    elif j==2:
        print("! ! ! Thank You ! ! !")
        break