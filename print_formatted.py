def print_formatted(number):
    # your code goes here
    h = []
    b = []
    o = []
    for i in xrange(1,number+1):
        h.append(hex(i)[2:].upper())
        b.append(bin(i)[2:])
        o.append(int(oct(i)))
    w = len(b[-1])
    for i in xrange(number):
        print str(i+1).rjust(w,' ' )+str(o[i]).rjust(w+1,' ')\
            +(str(h[i]).rjust(w+1,' ')).upper()+str(b[i]).rjust(w+1,' ')

if __name__ == '__main__':
    #n = int(raw_input())
    print_formatted(17)