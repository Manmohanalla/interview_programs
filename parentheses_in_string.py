
def parentheses_in_string(s):

    lst=[]
    l_node = '([{<'
    r_node = ')]}>'
    for i in s:
        if i in l_node or i in r_node: 
            print i
            if i in l_node:
                lst.append(i)
            elif len(lst) == 0:
                pass
            elif ord(i)-2==ord(lst[-1]) or ord(i)-1==ord(lst[-1]):
                lst.pop()
            else:
                return False
    return True

print parentheses_in_string('dscsd(({[dxscd]}<>)sxssx#[])')

