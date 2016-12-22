def anagramSolution2(s1,s2):
	alist1 = list(s1.lower())
	alist2 = list(s2.lower())

	alist1.sort()
	alist2.sort()
	while ' ' in alist1:
		alist1.remove(' ')
	while' ' in alist2:
		alist2.remove(' ')
	if alist2 == alist1:
		return True
	return False

#print(anagramSolution2('apple@ rEc 2 e#','elpap reec2 @#'))

def anagramSolution(s1,s2):

	s1= s1.replace(' ','')
	s2= s2.replace(' ','')
	s1=list(s1.lower())
	s2=list(s2.lower())
	if (len(s1) == len(s2)):
		while len(s1)>0:
			x=s1.pop()
			try:
				s2.remove(x)
			except:
				return False
		return True
	return False
	
print(anagramSolution('apple  @rnmm Ec2e#','elpa  preec mnm2@#'))

def anagramSolution4(s1,s2):
	c1 = [0]*26
	c2 = [0]*26

	for i in range(len(s1)):
		pos = ord(s1[i])-ord('a')
		c1[pos] = c1[pos] + 1

	for i in range(len(s2)):
		pos = ord(s2[i])-ord('a')
		c2[pos] = c2[pos] + 1

	j = 0
	stillOK = True
	while j<26 and stillOK:
		if c1[j]==c2[j]:
			j = j + 1
		else:
			stillOK = False

	return stillOK

#print(anagramSolution4('apple','pleap'))
