# def isPrime(n):
#    if n == 1:
#       return False
#    print n
#    for t in range(2,n):
#     	print n,t
#         if n % t == 0:
#           return False
#    return True

# print [n for n in range(1,100) if isPrime(n)]


def isPrime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    print n
    for t in range(3, int((n**0.5)+1),2):
    	print n,t
        if n % t == 0:
            return False
    return True

print [n for n in range(10) if isPrime(n)]