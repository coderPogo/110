import random


response = input("Do you want to roll a dice?")

while response == "y":

    
    no = random.randint(1,6)
    
    if no == 1 :
        print("")
        print("   X   ")
        print("")
    
    if no == 2 :
        print("X      ")
        print("")
        print("      X")
    
    if no == 3 :
        print("X      ")
        print("   X   ")
        print("      X")
    
    if no == 4 :
        print("X     X")
        print("")
        print("X     X")
    
    if no == 5 :
        print("X     X")
        print("   X   ")
        print("X     X")
    
    if no == 1 :
        print("X  X  X")
        print("")
        print("X  X  X")
    response = input("Do you want to roll a dice?")
    

