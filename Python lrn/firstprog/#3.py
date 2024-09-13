l = [input("Enter the first value")]
i=1
while i > 0:
    print("select choice "
          "Keep adding ?"
          "y or n")
    a = input()
    if a == "y":
        a = input("Enter input")
        l.append(a)
    elif a == "n":
        i = 0
for item in l:
    if item.isnumeric() and int(item)>=6:
        print(int(item))