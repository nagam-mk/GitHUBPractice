import re
count=0
str=input('Enter str:')
pattern=re.compile(str)
matcher=pattern.finditer('abbbabab')
for m in matcher:
    count+=1
    print('start:{}, end:{} and group:{}'.format(m.start(),m.end(),m.group()))
print('No. of occurance:',count)

#...............char classes:
matcher2=re.finditer('[a-z]','abcgs67@3xy')
for m2 in matcher2:
    print(m2.start(),'Matched:',m2.group())
#...................Match()
s=input('Enter search string:')
s1=input('Enter finding string:')
m=re.search(s,s1)
if m!=None:
    print('Match is available at begning of the string..!')
    print('Start index:',m.start(),'end index:',m.end(),'search string:',m.group())
else:
    print('Match is Not available at begning of the string..!')