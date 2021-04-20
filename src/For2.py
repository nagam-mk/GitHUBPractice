x=input('Enter mobile number:')
y=input('Enter number to find No. of times repeted:')
a=0
i=0
for i in x:
    if i==y:
        a=a+1
print('{} is repeted in {} times'.format(y,a))

