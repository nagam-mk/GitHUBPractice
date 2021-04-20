def decor(fun):
    print('starting deco')
    def inner(name):
        print('Name is:',name)
        if name=='Murali':
            print('Hello Murali Very good morning...!')
        else:
            fun(name)
    print('this is out side innner:',inner)
    return inner
print('test display')
@decor
def wish(name):
    print('Hello',name,'good morning')
print('before wish function')
wish('Neethu')