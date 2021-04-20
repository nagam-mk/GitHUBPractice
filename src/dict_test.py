s=input('Enter string:')
v=['a','e','i','o','u']
d={}
for x in s:
    if x in v:
        d[x]=d.get(x,0)+1
for k,v in sorted(d.items()):
    print(k,'is occurred',v,'times')
