'''write a code that slices the string (which is an input), append it to a list, count the number of each letter - and if it is identical to the letter before it, don't put it in the list, but rather increase the appearance number of that letter in the one before.
function([['a', 1], ['s', 2], ['a', 1], ['s', 2]], ['i', 1], ['n', 1])
word = 'commodore'

[('c', 1), ('o', 1), ('m', 2), ('o', 1), ('d', 1), ('o', 1), ('r', 1), ('e', 1)]'''

def concecutive(string):

	#converting string to lowercase
	string = string.lower()

	last= ''
	new= []

	for char in string:
		if char == last:
			new[-1] = (char,new[-1][1]+1)
		else:
			new.append((char,1))
			last = char
	return new
#print concecutive('commodore')

def count(string):

	cnt = [string[0],1]
	output = [cnt]

	for char in string[1:]:
		if char ==cnt[0]:
			cnt[1] +=1
		else:
			cnt = [char,1]
			output.append(cnt)
	return output

print count('oommodore')




