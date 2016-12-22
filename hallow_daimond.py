def daimond(num):
	n = num//2; 
	print n
	return ('\n'.join([''.join([('*' if abs(x)+abs(y) == n else ' ') for x in range(-n, n+1)]) for y in range(-n, n+1)]))
print daimond(3)
