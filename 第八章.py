class MuffledCalculator:
	muffled = False
	def calc(self,expr):
		try:
			return eval(expr)
		except:
			if self.muffled:
				print 
			else:
				raise


try:
	...
except (ZeroDivisionError,TypeError),e:
	print e

