phonebook={'alice':'1234','beth':'1,2,3,4'}

items=[('name','chen'),('age',23)]
d=dict(items)
d=dict(name='chen',age=23)

"alice's tele phone number is %(alice)s" % phonebook

---

x={}
y=x
x['name']='chen'
x={}
y这时不变

---

x={}
y=x
x['name']='chen'
x.clear()
y这时为{}

---
copy和deepcopy
copy是浅拷贝，替换的时候原始字典不受影响，但是修改的时候（比如删除），
原始字典也会受到影响
deepcopy是深拷贝，复制之后和原始的字典没有任何关系，修改也不会影响
from copy import deepcopy
dc=deepcopy(c)


## fromkeys
dict.fromkeys(['name','age'])
{}.fromkeys(['name','age'])


##items iteritems
d={'name':'chen','age':23}
d.items()
[('name','chen'),('age',23)]
list(d.iteritems())返回的是一个迭代器


##setdefault
d.setdefault('name','N/A')
有值的时候返回值，没有的话设置为第二个参数的值(N/A)


