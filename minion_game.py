def minion_game(string):
    '''
    banana
    '''
    kevin = 0
    stuart = 0
    ovel=['A','E','I','O','U']
    string = list(string)
    for index,i in enumerate(string):
        #print i
        if i in ovel:
            kevin = kevin + len(string)-(index+1)+1
            #print kevin
        else:
            stuart = stuart + len(string) - (index+1)+1
            #print stuart
    if kevin>stuart:
        print 'Kevin',kevin
    elif kevin == stuart:
        print 'Draw'
    else:
        print 'Stuart',stuart
if __name__ == '__main__':
    s = 'BANANA'
    minion_game(s)