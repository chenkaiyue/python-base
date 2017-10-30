迭代器
class Fibs:
	def __init__(self):
		self.a = 0
		self.b = 1
	def next(self):
		self.a,self.b = self.b,self.a+self.b
		return self.a
	def __iter__(self):
		return self

fibs=Fibs()
可以在for循环中使用
for f in fibs:
	if f > 1000:
		print f
		break

class TestIterator:
	value=0
	def next(self):
		self.value += 1
		if self.value > 10:
			raise StopIteration
		return self.value
	def __iter__(self):
		return self
ti = TestIterator()
list(ti)


八皇后问题
def queens(num=8,state=()):
	for pos in range(num):
		if not conflict(pos,state):
			if len(state) == num - 1:
				yield (pos,)
			else:
				for result in queens(num,state+(pos,)):
					yield (pos,result)

