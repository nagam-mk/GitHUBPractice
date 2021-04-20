s=input('Enter string:')
s1=''
x=0
i=0
a=0
while x<=len(s)-1:
    if s[x].isnumeric():
        b=eval(s[x])-1
        s1=s1+(b*s[x-1])
        i=i+1
        x=x+1
    else:
        s1=s1+s[x]
        x=x+1
print(s1)
#other way of same result
output=''
for j in s:
    if j.isalpha():
        output=output+j
        pre=j
    else:
        output=output+pre*(int(j)-1)
print(output)
#unicode to char
str=input('Enter string:')
out=''
for j in str:
    if j.isalpha():
        out=out+j
        last=j
    else:
        out=out+chr(ord(last)+int(j)) #if input a4d2 =>a((a=97 + 4)==e)d((d=100 + 2)==f, output=aedf
print(out)






