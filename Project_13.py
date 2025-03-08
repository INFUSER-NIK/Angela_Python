import random 

print("this is a coin toss program")

input("make your choice Head or Tail ")
coin = random.randint(1,2)
if coin == 1:
    print("head")
else :
    print("tail") 