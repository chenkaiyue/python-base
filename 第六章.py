callable(math.sqrt)

def fibs(nums):
	result=[0,1]
	for i in range(nums-2):
		result.append(result[-2]+result[-1])
	return result


文档化函数
def square(x):
	'calculate square'
	....
square.__doc__
help(square)




def store(data,full_name):
	names=full_name.split()
	if len(names) == 2:
		names[1:1] = ''
	labels = 'first','second','third'
	for label,name in zip(labels,names):
		people = lookup(data,label,name)
		if people:
			data[label][name].append(full_name)
		else:
			data[label][name] = [full_name]

def lookup(data,label,name):
	return data[label][name]

def init(data):
	data['first'] = {}
	data['second'] = {}
	data['third'] = {}

关键字参数
def hello(greeting='hello',name='world'):
	print "%s,%s"% (greeting,name)

def hello4(name,greeting='hello',punctuation='!')

收集参数
def print_params(title,*params):
print_params('params',1,2,3)
(1,2,3)作为元组传递给了params
def print_params2(x,y,z=3,*pospar,**keypar)
print_params2(1,2,3,4,5,6,foo=1,bar=2)
keypar存储的是{'foo':1,'bar':2}

def story(**kwds):
	return "there was a %(job)s called %(name)s" % kwds
story(job='language',name=python)
argv={'job':'language','name':'python'}
story(**argv)


访问全局变量(函数中有和全局变量重名的变量)
def combine(para):
	print para+globals()['para']

x=1
def change_global():
	#调用全局变量
	global x
	x += 1

闭包
def multipier(factor):
	def multiplyByFactor(number):
		return number * factor
	return multiplyByFactor


递归
def power(x,n):
	if n == 0:
		return 1
	else:
		return x * power(x,n-1)

def factorial(n):
	if n == 1:
		return 1
	else:
		return n * factorial(n-1)

函数式编程
map(str,range(10))
filter(lambda x:x.isalnum(),seq)
reduce(lambda x,y:x+y,numbers)


