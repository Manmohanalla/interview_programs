#!/usr/bin/env python
'''
Given a string, find the minimum number of characters to be inserted to convert it to palindrome.
For Example:
ab: Number of insertions required is 1. bab or aba
aa: Number of insertions required is 0. aa
abcd: Number of insertions required is 3. dcbabcd

Input:

The first line of input contains an integer T denoting the number of test cases.
The first line of each test case is S.

Output:

Print the minimum number of characters.

Constraints:
Example:

Input:
3
abcd
aba
geeks

Output:
3
0
3
'''
'''
babc / abcb
cbabc / abcbc
'''

def conv_palindrome(word,x=0):
    if len(word) <= 1:
        return 0
    if word == word[::-1]:
        return 0
    temp1=word
    temp2=word
    length = len(word)
    for index,i in enumerate(word[1:]):
        temp = word[index:length]
        if temp == temp[::-1]:
            return index
        temp1 = i+temp1
        temp2 = temp2+word[-2-index]
        temp3 = word[0:-1-index]
        if temp3 == temp3[::-1]:
            return index+1
        if temp2==temp2[::-1]:
            return x+1
        if temp1 == temp1[::-1]:
            return x+1
        x+=1
    return x

def input_palindrom():
    try:
        test_cases= int(raw_input("please enter the number of test cases: "))
    except ValueError:
        print 'Please Try again. Numeric values are only allowed'
        return input_palindrom()
    else:       
        lst=[]
        for i in xrange(test_cases):
            word = raw_input("Please enter test case no "+str(i+1)+':')
            lst.append(word)
        for word in lst:
            print conv_palindrome(word)

if __name__ == '__main__':
    input_palindrom()

