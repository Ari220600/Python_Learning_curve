'''Coder's Proposal Using Python'''
''' * * * * * * * * * * * * * * '''

print("WILL YOU BE MINE ?")
a=input("yes OR no:-")
if a!='yes' and a!= 'no':
    print("Wrong answer 😞😞,please try again")
def my_heart():
    for row in range(6):
        for col in range (7):
            if(row==0 and col%3!=0)or (row==1 and col%3==0) or (row-col==2)or (row+col==8):
                print("❤",end="")
            else:
                print("  ",end="")
        print()
def write_feeling():
    print("\nI LOVE YOU")
if a=='yes':
    my_heart()
    write_feeling()
def my_broken_heart():
    for row in range(6):
        for col in range(7):
            if row == 0 and col % 3 != 0 or row == 1 and col % 3 == 0 or row - col == 2 or row + col == 8:
                print("💔",end="")
            else:
                print(" ", end=" ")
        print()


def write_sad_feeling():
    print("\nALL THE BEST FOR YOUR LOVE LIFE 😞")

if a=='no':
    my_broken_heart()
    write_sad_feeling()