print("A tip calculater ")
bill = int(input("Total amount = "))
tip = int(input("tip percentage choice 0,10,12,15,100,1000 \n"))
tip_a = round((bill*tip)/100,2)
split = int(input("How many people have eaten = "))
split_a = round((bill+tip_a)/split,2)
print(f"Paybal bill for each person = {split_a}")
