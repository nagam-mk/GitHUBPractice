
s=(input('Enter your name:'))
x=0
for i in s:
    print('S[{}]/S[{}] is {}'.format(x,x-len(s),i))
    x=x+1