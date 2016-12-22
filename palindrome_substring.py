from datetime import datetime 
import enchant

def palindrome_substring(input):
	lst=[]
	lng=''
	input=input.replace(' ','')
	#print input
	start = datetime.now()
	for i in xrange(0,len(input)-1):
		for j in xrange(i,len(input)):
			print input[j:i-1:-1]
			x = input[i:j+1]
			#print x
			d = enchant.Dict('en_US')
			if input[i:j+1] == x[::-1] and len(x)>1:
				if d.check(x):
					if len(x)>len(lng):
						lng = x
					lst.append(x)
	print lst,lng
	now = datetime.now()
	print now-start
palindrome_substring('civicxxx')
