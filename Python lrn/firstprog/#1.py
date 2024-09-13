# Create a dictionary and take input from the user and return the meaning of the
# word from the dictionary
a=input("enter the First word ")
a.capitalize()
b=input("Enter the meaning")
b.capitalize()
d={a:b}
a=input("enter the second word ")
a.capitalize()
b=input("Enter the meaning")
b.capitalize()
d[a]=b
a=input("enter the third word ")
a.capitalize()
b=input("Enter the meaning")
b.capitalize()
d[a]=b
a=input("enter the fourth word ")
a.capitalize()
b=input("Enter the meaning")
b.capitalize()
d[a]=b
a=input("enter the fifth word ")
a.capitalize()
b=input("Enter the meaning")
b.capitalize()
d[a]=b
a=input("Enter the word you want to know")
a.capitalize()
print("The meaning of ",a,"is",d[a])
