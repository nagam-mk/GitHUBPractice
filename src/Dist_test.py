#count no of times repeted the each char in given string
s=input('Enter the strin:')
d={}
for x in s:
    if x in d.keys():
        d[x]=d[x]+1
    else:
        d[x]=1
  #now the given string converted into dictionary format with key and value(no of times repeted)
  #i.e if str=aaabaacc==>{'a'=5,'b'=1,'c'=2}
for k,v in d.items():
    print('{}={} times'.format(k,v))

