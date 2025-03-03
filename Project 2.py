print("The BMI calculater")
a=int(input("Enter your weight = "))
b=float(input("Enter your height in meter = "))
c=round(a/(b**2),2)
print("your BMI is = ",float(c))
if c < 18.5:
    print("underweight")
elif c > 18.5 and c < 25:
    print("normal weight")
elif c > 25 and c < 30 :
    print("over weight")
elif c > 30 and c < 35:
    print("obese")
else:
    print("clinically obese")