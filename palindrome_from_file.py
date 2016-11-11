def palindrome_file(filename):

    with open(filename) as f:
    	lines = f.read().splitlines()

    line_no=0
    for line in lines:
    	line_no +=1
    	line = line.lower()
        if line == ''.join(reversed(line)):
            print line_no,line
            
palindrome_file('palindrome_file.txt')