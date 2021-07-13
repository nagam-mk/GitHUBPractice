import time
def fib():
    a,b=0,1
    while True:
        yield a
        a,b=b,a+b
for f in fib():
    print(f)
    time.sleep(1)