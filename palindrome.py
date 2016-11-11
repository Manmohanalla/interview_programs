
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

def is_palindrome(word):

    letters = list(word)
    is_palindrome = True

    for letter in letters:
        if letter == letters[-1]:
            letters.pop(-1)
        else:
            is_palindrome = False
            break

    return is_palindrome