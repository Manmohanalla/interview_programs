d ={'a':1,'c':{'g':7,'d':{'e':5,'f':6}},'b':10}

def flatten(d,prefix='',output={}):

	for key,value in d.items():
		#print key,value
		if type(value)==dict:
			new_prefix = prefix + key + '.'
			flatten(value, new_prefix)
		else:
			key = prefix+key
			output.update({key:value})
	return output
print flatten(d)