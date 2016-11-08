'''Using the higher order function reduce(), write a function max_in_list() that 
takes a list of numbers and returns the largest one.'''

def max_in_list(lst):

	max_numb = reduce((lambda x,y:max(x,y)),lst)
	return max_numb


def maxi(lst):

	maximum = lst[0]
	for i in lst:
		if i > maximum:
			maximum=i
	return maximum
