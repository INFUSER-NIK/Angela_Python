print("a billing pizza machine")
s = "small pizza = 150"
m = "medium pizza = 300"
l = "large pizza = 600"

pep_small = "pep for small pizza = 20"
pep_m_l = "pep for mid and large = 50"

c = "extra cheese for pizza = 10"

print(f"{s}\n{m}\n{l}\n\n{pep_small}\n{pep_m_l}\n\n{c}\n")

size = input("make youe choice : ")
no_of_pizza = int(input("How many do you want :"))
pep = input("add pep Y or N : ")
cheese = input("extra cheese Y or N : ")

bill = 0

if size == "s":
    bill =  150*no_of_pizza
    if pep == "Y":
        bill += 20
elif size == "m":
    bill = 300*no_of_pizza
    if pep == "Y":
        bill += 50
elif size == "l":
    bill = 600*no_of_pizza
    if pep == "Y":
        bill += 50

if cheese == "Y":
    bill += 10

    
print("your total amount = ",bill)