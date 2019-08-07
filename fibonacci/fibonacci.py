import time

vals = [1,1]

def fib_next():
    global vals
    if vals[0] >= vals[1]:
        newval = 1
    else:
        newval = 0
    vals[newval] = vals[0]+vals[1]

def print_fib(arry):
    fib_next()
    print(max(arry))

while True:
    print_fib(vals)
    time.sleep(0.2)