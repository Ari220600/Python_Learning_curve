"""
Stone Paper Sissor
Now moving on to instructions:
You have to use a random choice function that we studied in tutorial #38, to select between, snake, water, and gun.
You do not have to use a print statement in case of the above function.
Then you have to give input from your side.
After getting ten consecutive inputs, the computer will show the result based on each iteration.
You have to use loops(while loop is preferred).
"""
import random
print("\n\t\t\t ********** WELCOME TO STONE || PAPER || SCISSORS GAME ************\n")
i=0
pc=0
pl=0
list=[[""],["Stone"],["Paper"],["Sissors"]]
print("*There will be 10 rounds")
while i<10:
    print("Round",i+1,"Begins")
    try:
        ip=int(input("Press 1: Stone\nPress 2: Paper\nPress 3: Sissors\n"))
    except:
        print("invalid input\n")
        continue
    if 3<ip or ip<1:
        print("invalid input")
        continue
    print("\nYour choice:",list[ip])
    rand=random.randint(1,3)
    print("\nchoice of pc:",list[rand])
    if ip==rand:
        print("\nThe round is a Draw\n")
    elif ip==3 and rand==1:
        pc+=1
        print("\nPoint goes to pc\n")
    elif rand==3 and ip==1:
        pl+=1
        print("\nPoint goes to player\n")
    elif rand==ip+1:
        pc+=1
        print("\nPoint goes to pc\n")
    elif ip==rand+1:
        pl+=1
        print("\nPoint goes to player\n")
    i+=1
print("Score:\n\t\tPlayer\t\t\t\tPC\n\t\t",pl,"\t\t\t\t   ",pc)
if pl>pc:
    print("\nCongratulations You Are The Winner")
elif pc==pl:
    print("\nThe game is a draw, Better luck next time")
else:
    print("\nPc is the winner, Better luck next time")