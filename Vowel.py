def vowel(char):
	
	# reads a line from input
	char = char.lower()

	# Check if a character
	if len(char)!=1 or not char.isalpha():
		return 'Only 1 alpha character is allowed'

	# vowels
	vowels = 'aeiou'

	# condition to check if vowel
	if char in vowels:
		return True
	else:
		return False


