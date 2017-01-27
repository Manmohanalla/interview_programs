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
        temp3 = word[0:-1-index]
        if temp3 == temp3[::-1]:
            return index+1
        temp1 = i+temp1
        if temp1 == temp1[::-1]:
            return x+1
        temp2 = temp2+word[-2-index]
        if temp2==temp2[::-1]:
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

