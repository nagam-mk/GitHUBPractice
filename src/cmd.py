a,b,c=10,20,30
print("The SUM:",a,b,c)
print()
print("The SUM:",a,b,c,sep='/')

a,b,c=[int(x) for x in input('Enter 3 values:').split(',')]
print(a+b+c)
i=1
while i<=10:
    print('Number:',i)
    i=i+1
