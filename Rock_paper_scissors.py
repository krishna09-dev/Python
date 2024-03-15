import random
print("Hey Well-come to Rock,Paper,Scissor")
print("Chose your choice Rock , Paper or Scissors")
a=input("Enter your choice")
b= random.choice(["Rock", "Paper", "Scissors",])
if (a==b):
    print("its a tie")
elif(a=="rock"):
    if(b=="paper"):
        print("Your choice : "+ a)
        print("computer choice : "+ b)
        print("you lost")
        
elif(a=="paper"):
    if(b=="rock"):
        print("Your choice : "+ a)
        print("computer choice : "+ b)
        print("you won")
        
elif(a=="scissor"):
    if(b=="rock"):
        print("Your choice : "+ a)
        print("computer choice : "+ b)
        print("you lost")
        
elif(a=="rock"):
    if(b=="scissor"):
        print("Your choice : "+ a)
        print("computer choice : "+ b)
        print("you won")
        
elif(a=="scissor"):
    if(b=="paper"):
        print("Your choice : "+ a)
        print("computer choice : "+ b)
        print("you won")
        
elif(a=="paper"):
    if(b=="scissor"):
        print("Your choice : "+ a)
        print("computer choice : "+ b)
        print("you lost")
        
else:
    print("Check the spelling")
    

        
        
