# Math24 solver in Python
# JH@KrappLab
# 2015-12-01

import itertools  
import __future__

print "\nSearching for answers ... \n"
numlist = list(set(map("".join,itertools.permutations('XJQK')))) 
#print numlist
oplist = list(map("".join,itertools.product('+-*/', repeat=3)))
#print oplist

for i in numlist:
	for j in oplist:
		for k in range(5):
			if k == 0: # '123':
				exp = ( '((('+i[0] + j[0] + i[1]+')' + j[1] +i[2]+')' + j[2] +i[3]+')' )
			elif k == 1: #'132' or k =='312':
				exp = ( '(('+ i[0] + j[0] + i[1]+')' + j[1] +'('+i[2] + j[2] +i[3]+'))' )
			elif k == 2: #'213':
				exp = ( '(('+i[0] + j[0] + '('+ i[1] + j[1] +i[2]+'))' + j[2] +i[3]+')' )
			elif k == 3: #'231':
				exp = ( '('+ i[0] + j[0] + '(('+ i[1] + j[1] +i[2]+')' + j[2] +i[3]+'))' )
			elif k == 4: #'321':
				exp = ( '('+ i[0] + j[0] +'('+ i[1] + j[1] +'('+i[2] + j[2] +i[3]+')))' )	

			exp = exp.replace('X','10');exp = exp.replace('J','11');exp = exp.replace('Q','12');exp = exp.replace('K','13');

			try:
				res = eval(compile(exp,'<string>','eval', __future__.division.compiler_flag))
			except ZeroDivisionError:
				pass	#print "Warning: NaN encoutered!"	

			if res == 24.0:
				print exp,'=', res

print "\nEnd of searching !"
