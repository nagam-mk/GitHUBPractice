#Example 1
s=input("Enter string:")
i=0
for x in s:
    print("The cahr at {} Position is {}".format(i,x))
    i=i+1
#Example 2
for i in range(20,0,-1):
    print(i)
a = int(input("Enter 1st Value:"))
#Example 3
list=eval(input("Enter list of numbers:"))
sum=0
for n in list:
    sum=sum+n
print("Sumb of list of numbers:",sum)

for m in range(4):
    for n in range(4):
        print(m,n)

