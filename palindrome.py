
def palindrome(my_str):
	
	#converting string to lower cases
	my_str = my_str.lower()
	# reverse the string
	rev_str = reversed(my_str)
	# check if the string is equal to its reverse
	if list(my_str) == list(rev_str):
		return True
	else:
		return False

def palindrome1(my_str):

	#converting string to lower cases
	my_str = my_str.lower()
	#reading list from the last character and comparing
	if my_str[::-1] == my_str:
		return True
	else:
		return False

def is_palindrome(string):

    is_palindrome = True

    for i in xrange((len(string)+1)/2):
        if string[i] == string[-i-1]:
        	print string[i],string[-(i+1)]
        else:
            is_palindrome = False
            break

    return is_palindrome
print is_palindrome('radar civic radar')