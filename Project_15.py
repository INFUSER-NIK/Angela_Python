import random 

letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers = ['1','2','3','4','5','6','7','8','9','0']
symbol = ['!','@','#','%','&','*']

print("Welcome to password generator")

ask_1 = int(input("how many letters needed in password\n"))
ask_2 = int(input("how many numbers needed in password\n"))
ask_3 = int(input("how many symbol needed in password\n"))

r11 = ""
for i in range(0,ask_1):
    r1 = random.choice(letters)
    r11 += r1
print(r11)

r22 = ""
for n in range(0,ask_2):
    r2 = random.choice(numbers)
    r22 += r2
print(r22)

r33 = ""
for m in range(0,ask_3):
    r3 = random.choice(symbol)
    r33 += r3
print(r33)

rf = r11 + r22 + r33
print(rf)

ask_total = len(rf)

password = ""
for d in range (0,ask_total):
    r44 = random.choice(rf)
    password  += r44
print("your NASA made password is :\n",password)