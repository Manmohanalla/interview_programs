

def fib(i, h):
    j = i+h
    i = h
    h = j
    if h < 100:
        return fib(i, h)
print fib(0,1)

def rec_fib(n):
    '''inefficient recursive function as defined, returns Fibonacci number'''
    if n > 1:
        return rec_fib(n-1) + rec_fib(n-2)
    return n
#print rec_fib(4)