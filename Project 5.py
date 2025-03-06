print("WAP for even and odd number")
a = int(input("write the year of your choice \n"))
if a % 4 == 0:
    if a % 100 == 0:
        if a % 400 == 0:
            print("leap year")
        else:
            print("not a leap year")    
    else:
        print("leap year")        
else:
    print("not a leap year")

