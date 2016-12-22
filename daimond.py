#!/usr/bin/python

def getInput():
    number = raw_input("Enter an odd number or hit ENTER to quit program: ")
    
    #number =3
    if (not number):
        return -2
    try:
        n = int(number)
    except:
        print "\nPlease input only integer numbers\n"
        return 0
    if not n:
        print "\nCannot print symbols for a zero value, try again.\n"
    
    return n
def daimond():

    n = getInput()    
    for i in range(1, n+1, 2):
        print ("*" * i).center(n)
    for i in range(1, n-1, 2):
        print ("*" * (n - (i + 1))).center(n)
    print "\nQuitting program...\n"

if __name__ == "__main__":
    
    daimond()
