'''searching ip address from log file'''
import re

def log_search(f_name):
	lst=[]
	with open(f_name,'rb') as f:
		for i in f:
			x= (i).split(' ')[0]
			lst.append(x)
		print set(lst)
log_search('nginx_access.log')