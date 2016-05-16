import winsound
#winsound.Beep(440,500)
import numpy as np
import sys
import time
'''
for i in '31415926':
	winsound.Beep(int(i)*100,200)
'''
'''
for i in range(1000):
	winsound.Beep((np.random.randint(9)+1)*100,200)
	if i % 10==0:
		print i
'''
from decimal import *
getcontext().prec=1000
#seq=str(Decimal(3).sqrt()).replace('.','')
'''
musicnum=7
if len(sys.argv)>1:
	musicnum=float(sys.argv[1])
seq=str(Decimal(musicnum).sqrt()).replace('.','')
'''
seq=str(Decimal(1).exp()).replace('.','')

#print seq
print 'Now play...'

note_list=[0,2,4,5,7,9,11,12 ,14,16]
for num in seq: 
	sys.stdout.write(num)
	num=int(num)
	if num == 0:
		time.sleep(0.200)
	else:
		note = int(2**(note_list[num-1]/12.0)*261)
		winsound.Beep(note,200)

