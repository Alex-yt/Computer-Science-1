# Fortune Cookie program
# Imports
#homework
#self taught

Name = input("Hello please input your name to see your fortune.")
import random


fortune = random.randint(1, 5)

fortune_1 = "Hard work should never be stomped on"
fortune_2 = "knolege is more then one scent"
fortune_3 = "Your the one who makes choices"
fortune_4 = "Don't be judgemental it will hit you later in life"
fortune_5 = "You make one its your path you follow"

if fortune == 1 :
    print(Name  + "your fortune is: " + fortune_1)
elif fortune == 2 :
    print(Name  + "your fortune is: " + fortune_2)
elif fortune == 3 :
    print(Name  + "your fortune is: " + fortune_3)
elif fortune == 4 :
    print(Name  + "your fortune is: " + fortune_4)
elif fortune == 5 :
    print(Name  + "your fortune is: " + fortune_5)
else :
    print("sry man ran out gl GO STUDY")

    
    restart = input("Would you like to restart this program?")
    if restart == "yes" or restart == "y":
        script()
    if restart == "n" or restart == "no":
        print ("Script terminating. Goodbye.")
script()
input("\n\nPress the Enter key to exit.")
