s=input('Enter String:')
i=len(s)-1
print(i)
while i>=0:
    print(s[i],end='')
    i=i-1
print()
#Reverse the words in given string in same order
name=input('Enter string:')
l=name.split()
l2=[]
x=0
y=len(l)-1
while x<=y:
    l1=''.join(reversed(l[x]))
    l2.append(l1)
    x=x+1
output=' '.join(l2)
print(output)
#print Odd and even postion letters from given string
s=input('Enter string:')
a=len(s)-1
i=0
even=''
odd=''
while i<=a:
    if (i%2)==0:
        print(s[i])
        even=even+s[i]
    else:
        odd=odd+s[i]
    i=i+1
print('Even:',even)
print('Odd:',odd)
