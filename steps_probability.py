#!/usr/bin/python

def calculate_steps(n):
	if (n <= 1):
	   	return n
	return calculate_steps(n-1) + calculate_steps(n-2)

def no_steps(n):
	n+=1
	return calculate_steps(n)

if __name__ == '__main__':
	print no_steps(10)