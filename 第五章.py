from module1 import open as open1
from module2 import open as open2

序列解包，元组
key,value=phonebook.popitem()

assert 0<age<100 'the age must be realistic'

for key,value in d.items():
	print key,'corresponds to ',value


name=['chen','li']
age=[23,24]
zip(name,age)
[('chen',23),('li',24)]
for name,key in zip(name,key):
	print name+':',age

enumerate 索引-值对
for index,string in enumerate(strings):
	if 'aaa' in string:
		strings[index] = '111'


[x*x for x in range(10) if x % 3 == 0]


letterGirls={}
for girl in girls:
	letterGirls.setdefault(girl[0],[]).append(girl)
print [b+'+'+g for b in boys for g in letterGirls[b[0]]]


##作用域
scope={}
exec 'sqrt=1' in scope
scope['sqrt']

eval(raw_input("enter expression:"))

scope={}
exec 'x=2' in scope
eval('x*x',scope)

scope={}
scope['x'] = 2
scope['y']=3
eval('x*y',scope)