'''Given an input integer, find the next larger integer with 3 and 6 as the digits

Example 123, output: 333
Example 456, output: 633
Example 345, output: 363'''

def next_largest(input,x=0):
	y=x+1
	print x,y
	if input not in range(0,666):
		return 'not in range'
	elif input<333:
		return 333

	lst=[333,336,363,366,633,636,663,666]

	if input in range(lst[x],lst[y]+1):
		return lst[y]
	else:
		x+=1
		return next_largest(input,x)
	#return lst[y]
print next_largest(665)