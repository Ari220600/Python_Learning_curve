#1. You are free to use anything we've studied till now.
#2. The number of guesses should be limited, i.e (5 or 9).
#3. Print the number of guesses left.
#4. Print the number of guesses he took to win the game.
#5. “Game Over” message should display if the number of guesses becomes equal to 0.
import random

a=random.randint(1,100)
n=1
print("\t\t! ! ! Welcome to Guessing game ! ! !\nRules:\nYou have to guess the number between 1 to 100 using the hint given after each guess within 9 tries")
while(n<=9):
    print("You have",10-n," chance left")
    inp=int(input("Enter your guess\n"))
    if inp>a:
        print("The number you guessed is GREATER than the correct answer")
    elif inp<a:
        print("The number you guessed is SMALLER than the correct answer")
    else:
        print("Congratulations You have guessed the correct number ",a," within",n,"chance\n\t\t! ! ! THANK YOU ! ! !")
        n=0
        break
    n+=1
if n!=0:
    print("The correct answer was",a,"\nBetter luck next time\n\t\t! ! ! THANK YOU ! ! !")