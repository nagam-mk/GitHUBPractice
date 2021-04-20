n=int(input("Enter number:"))
for i in range(n+1,0,-1):
    print('*'*i)

for j in range(1,n+1):
    print(' '*(n-j),end=' ')
    print('* '*j)
