##第三章
from string import Template
s = Template('$x,glorious $x')
s.substitude(x='slurm')

s=Template('a $thing must never $action')
d={}
d['thing'] = 'gentleman'
d['action'] = 'show his socks'
s.substitude(d)


'%s plus %s equals %s' % (1,1,2)

print('% 5d' % 10)


## 字符串方法
'hello kitty'.find('kitty')
'+'.join(['1','2','3'])
'TTTT'.lower()
"that's all fork".title()
'this is a test'.replace('is','ezz')
'1+2+3'.split('+')
'***spam*!spam!!!!'.strip('*!')

translate ##转换单个字符
from string import maketrans
table=maketrans('cs','kz')
'this is a test'.translate(table)
