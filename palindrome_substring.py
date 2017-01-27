
def palindrome_substring(input):
    lst=[]
    lng=''
    input=input.replace(' ','')
    for i in xrange(0,len(input)-1):
        for j in xrange(i,len(input)):
            # print input[j:i-1:-1]
            x = input[i:j+1]
            if input[i:j+1] == x[::-1] and len(x)>1:
                if len(x)>len(lng):
                    lng = x
                lst.append(x)
    print lng
palindrome_substring('banana')

def palindrome(word):
    if len(word) <=1:
        return word
    else:
        for i in range(len(word)):
            for j in range(0, i):
                sub_str = word[j:i +1]
                if sub_str == sub_str[::-1]:
                    print sub_str
                    
word  = "bana"                
palindrome(word)