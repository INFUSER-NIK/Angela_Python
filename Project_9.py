'''finding avarage height of the student
 using for loop '''

stu_name = input("list of the student heights : \n").split()


for n in range (0,len(stu_name)):
    stu_name[n] = int(stu_name[n])
print(stu_name)  

a=0
for i in range (0,len(stu_name)):
    a = a + stu_name[i]

avg_height = a/len(stu_name)
print("average height of the student is :",avg_height)