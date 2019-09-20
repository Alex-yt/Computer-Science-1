#homework
# starawberry popcorn
# idk

import random
WAY = input("Rock, Paper, or scissors?")
roll = random.randint(1, 3)

if roll == 1:print("rock")

elif roll == 2: print("paper")

elif roll == 3: print("scissors")


if WAY == "rock" and roll == 1 or WAY == "paper" and roll == 2 or WAY == "scissors" and roll == 3:
    print("wow your semi educated that you could tie with me congrats")

if WAY == "paper" and roll == 3 or WAY == "rock" and roll == 2 or WAY == "scissors" and roll == 1:
    print("Ha you filthy nub get good kid")

if WAY == "scissors" and roll == 2 or WAY == "paper" and roll == 1 or WAY == "rock" and roll == 3:
    print("wow fine you win now go away")

input("\n\nPress the enter key to exit.")
