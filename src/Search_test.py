import re
count=0
str=input('Enter mobile number :')
s=re.fullmatch('[6-9]\d{9}',str)

if s!=None:
    print('{} is valid mobile number'.format(str))
else:
    print('{} is Not valid mobile number'.format(str))
#---------------------------------------
import re
str=input('Enter mobile number :')
x=object()
l=len(str)

if l==10:
    x=re.fullmatch('[6-9]\d{9}',str)
elif l==11:
    x=re.fullmatch('[0][6-9]\d{9}',str)

elif l==12:
    x=re.fullmatch('[9][1][6-9]\d{9}',str)
elif l==13:
    x=re.fullmatch('[+][9][1][6-9]\d{9}',str)
if x!=None:
    print('{} is valid mobile number'.format(str))
else:
    print('{} is Not valid mobile number'.format(str))

