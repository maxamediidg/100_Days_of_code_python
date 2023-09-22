def calculate(n,**kwargs):
	print(type(kwargs))
	print(kwargs["add"])
	n += kwargs["add"]
	n *= kwargs["multiply"]
	print(n)


calculate(2,add=3, multiply=5)
calculate()

class car:

	def __init__(self, **kw):
		self.make = kw["make"]
		self.model = kw["model"]
my_car = car(make="nissan", model="GT-8")
print(my_car.model)