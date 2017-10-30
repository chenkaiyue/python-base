import sys
sys.path.append('c:/python')

export PYTHONPATH=$PYTHONPATH:~/python


import os
os.system('/usr/bin/firefox')


fileinput
import fileinput
for line in fileinput.input('''inplace=True'''):
	line = line.rstrip()
	num = fileinput.lineno()
	print "%-40s # %2i" % (line,num)



堆
from heapq import *
from random import shuffle
data=range(10)
shuffle(data)
heap = []
for n in data:
	heappush(heap,n)
heappop(heap)
heapreplace(heap,0.5)


双端队列
from collections import deque
q=deque(range(5))
q.append(5)
q.appendleft(6)
q.pop()
q.popleft()
q.rotate(3)


正则表达式
r'(http://)?(www\.)?python.org'
r'^ht+p'

 

import fileinput,re
pat = re.compile(r'From:(.*) <.*?>$')
for line in fileinput.input():
	m = pat.match(line)
	if m :
		print m.group(1)

