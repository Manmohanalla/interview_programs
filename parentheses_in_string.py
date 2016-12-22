
def parentheses_in_string(s):

    lst=[]
    l_node = '([{<'
    for i in s:
        if i in l_node:
            lst.append(i)
        elif ord(i)-2==ord(lst[-1]) or ord(i)-1==ord(lst[-1]):
            lst.pop()
        else:
            return False
    return True

print parentheses_in_string('(({[]}<>))')

