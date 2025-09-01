
list1=[]

n=int(input("Enter number of elements in list :"))
print(n)

for i in range(n):
    temp=int( input("Enter a nuber :") )
    if temp>0:
        list1.append(temp)


print(list1)