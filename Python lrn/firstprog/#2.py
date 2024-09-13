# Exercise 2 - Faulty Calculator
# 45 * 3 = 555, 56+9 = 77, 56/6 = 4
# Design a calculator which will correctly solve all the problems except
# the following ones:
# 45 * 3 = 555, 56+9 = 77, 56/6 = 4
# Your program should take operator  and the two numbers as input from the user
# and then return the result
while(1):
      print("Enter your operation : +, -, *, / ")
      b=input()
      if b=="+":
            a = int(input("Enter your first value"))
            c = int(input("Enter the second value"))
            if a==56 and c==9:
                  print(77)
            else:
                  print(a+c)

      elif b=="-":
            a = int(input("Enter your first value"))
            c = int(input("Enter the second value"))
            print(a-c)
      elif b=="*":
            a = int(input("Enter your first value"))
            c = int(input("Enter the second value"))
            if a==45 and c==3:
                  print(555)
            else:
                  print(a*c)
      elif b=="/":
            a = int(input("Enter your first value"))
            c = int(input("Enter the second value"))
            if a==56 and c==6:
                  print(4)
            else:
                  print(a/c)
      else:
            print("Invalid operation input")
      inp=input("press y to continue\nPress n to stop")
      if inp=="n":
            print("! ! ! Thank you ! ! ! ")
            break

