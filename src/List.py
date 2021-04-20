l=(10,20,10,'Murali',)
s={10,20,30,25}
fs=frozenset(s)
print(fs)
for i in fs:print(i)
s.add(50)
print(s)
print(fs)

print(l)
r=range(0,20,2)
for i in r: print(i)

def f1():
    for i in r: print('Murali \'Hello\'')
f1()
print(f1())
