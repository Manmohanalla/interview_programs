import math

def fizzbuzz(i, input=0):
	
	if type(i) != int:
		print 'Integer only'
	if i >= input:
		msg=''
		if input <= 3:
			print isPrime(input)
		else:
			if input%3 ==0:
				msg+='Fizz'
			if input%5 ==0:
				msg+='Buzz'
			if msg:
				print msg
			else:
				print isPrime(input)
		fizzbuzz(i,input+1)



def isPrime(num):
	if num <2:
		return num
	for i in range(2, int(math.sqrt(num)) + 1):
		if num % i == 0:
			return num
	return 'BuzzFizz'

if __name__ == '__main__':
	fizzbuzz(15)