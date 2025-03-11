stu_name = input("list of the student heights : \n").split()


for n in range (0,len(stu_name)):
    stu_name[n] = int(stu_name[n])
print(stu_name) 

a = 0
for i in stu_name:
    if a < i :
        a = i

print("max height of the student is :",a)