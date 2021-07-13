def decor1(num):
    def inner():
        x=num()
        return x*x
    return inner
def decor2(num):
    def inner():
        x=num()
        return 2*x
    return inner
@decor1
@decor2
def num():
    return 10
print(num())