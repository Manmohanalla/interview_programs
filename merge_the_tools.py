def merge_the_tools(string, k):
    # your code goes here
    lst=[]

    for i in xrange(1,(len(string)/k)+1):
        lst.append(string[:k])
        string = string[k:]
    for i in lst:
        l=list(i)
        for index,j in enumerate(l):
            while j in l[index+1:]:
                for index2, k in enumerate(l):
                    if index2>index and k==j:
                        l.pop(index2)
        print ''.join(l)
                        
if __name__ == '__main__':
    merge_the_tools('ABACAAADA', 3)