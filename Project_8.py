import random 
name = input("write the names of the people with coma  :")
names = name.split(",")
print(names)
namess = len(names)
card_picked = random.randint(0,namess-1)
print(f"{names[card_picked]} has to pay all the bill")