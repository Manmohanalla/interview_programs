'''The problem is finding the length of longest prefix given an array of strings.
Basically, write the following function:
int find_longest_prefix(char *strings[], int n)
If using Java you might not need n as Java arrays contain a length attribute.
Examples:
If the list consists of "total", "totem", "tote" the longest prefix is "tot" and the function should return 3
If the list consists of "total", "totem", "tote", "texas" the longest prefix is "t" and the function should return 1
If the list consists of "total", "totem", "tote", "texas", "cisco", the longest prefix is empty string and function should return 0.
The array will not be empty and there will be at least 1 string (as pre-condition)
'''
from datetime import datetime
import os

def prefix(lst):
	start = datetime.now()
	if len(lst)==0:
		return 0
	for i in xrange(len(lst[0])):
		print "i: %d" % i
		for string in lst[1:]:
			print "string: %s" % string
			if i >=len(string) or string[i] != lst[0][i]:
				print "answer: %s" % lst[0][:i]
				return len(lst[0][:i])
	return lst[0]



def prefix2(lst):
    "Given a list of pathnames, returns the longest common leading component"
    start = datetime.now()
    if not lst: return ''
    s1 = min(lst)
    s2 = max(lst)
    for i, c in enumerate(s1):
        if c != s2[i]:
            return len(s1[:i])
    return s1


if __name__ == '__main__':
	lst= ["total", "totem", "tote"]
	print prefix(lst)

	print prefix2(["total", "totem", "tote"])

	x=os.path.commonprefix(lst)
	print x
