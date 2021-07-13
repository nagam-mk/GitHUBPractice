def decor1(fun):
    def inner(name):
        print("Decor 1 executed....")
        fun(name)
    return inner
def decor2(fun):
    def inner(name):
        print("Decor 2 executed...")
        fun(name)
    return inner
@decor1
@decor2
def wish(name):
    print("This Main Wish function:", name)
wish("Murali")