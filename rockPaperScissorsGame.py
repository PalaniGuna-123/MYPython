import random
import sys 
from enum import Enum

class RPS(Enum):
        ROCK =1
        PAPER=2
        SCISSORS=3
              
print(" ")

playerChoice=input("Enter....\n1  Rock,\n2  Paper,\n3  scissors \n\n ")
print(playerChoice)
player=int(playerChoice)
if player<1 or player >3:
        sys.exit(" You must enter 1,2 or 3.")

coumputerChoice=random.choice("123")
computer=int(coumputerChoice)

print("")
print("you chose"+str(RPS(player)).replace('RPS.',"")+".")
print("python chose"+str(RPS(computer)).replace('RPS.',"")+".")
print("")


if player==1 and computer==3:
    print("👍😍😍😍you win!") 
elif player==2 and computer==1:
        print("👍😍😍😍you win!") 
elif player==3 and computer==2:
          print("👍😍😍😍you win!") 
elif player==computer:
         print("😁 Tie Game!") 

else:
        print("🐍🐍🐍🐍  Python Wins!")





