#!/usr/bin/env python
def conv_number(number):

    lst = list(number)
    for index,i in enumerate(lst):
        if i == '0':
            lst[index]='5'
    return ''.join(lst)

def convert():
    try:
        test_cases= int(raw_input("please enter the number of test cases: "))
    except ValueError:
        print 'Please Try again. Numeric values are only allowed'
        return convert()
    else:       
        lst=[]
        for i in xrange(test_cases):
            number = raw_input("Please enter test case no "+str(i+1)+':')
            try:
                num = int(number)
                number = str(num)
            except ValueError:
                print 'Please Try again. Numeric values are only allowed'
                return convert()
            lst.append(number)
        for number in lst:
            print conv_number(number)

if __name__ == '__main__':
    convert()