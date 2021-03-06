class TripleVector:
	x = 0
	y = 0
	z = 0

	def __init__(self, x, y, z):
		self.x = float(x)
		self.y = float(y)
		self.z = float(z)

	@staticmethod
	def zero():
		return TripleVector(0,0,0)

    # String represntation
	def __str__(self):
		return '<%s, %s, %s>' % (self.x, self.y, self.z)

	# Produce a copy of itself
	def __copy(self):
		return TripleVector(self.x, self.y, self.z)

	# Signing
	def __neg__(self):
		return TripleVector(-self.x, -self.y, -self.z)

	# Scalar Multiplication
	def __mul__(self, number):
		if(type(number) != int or type(number) != float):
			raise TypeError("Operand must be type int or float")

	# Division
	def __div__(self, number):
		if(type(number) != int or type(number) != float):
			raise TypeError("Operand must be type int or float")
			
		return self.__copy() * (number**-1)

	# Arithmetic Operations
	def __add__(self, operand):
		if(not isinstance(operand, TripleVector)):
			raise TypeError("Operand must be type TripleVector")
		return TripleVector(self.x + operand.x, self.y + operand.y, self.z + operand.z)

	def __sub__(self, operand):
		if(not isinstance(operand, TripleVector)):
			raise TypeError("Operand must be type TripleVector")
		return self.__copy() + -operand

	# Cross product
	# cross = a ** b
	def __pow__(self, operand):
		if(not isinstance(operand, TripleVector)):
			raise TypeError("Operand must be type TripleVector")

		return TripleVector(self.y*operand.z - self.z*operand.y, 
			                self.z*operand.x - self.x*operand.z, 
			                self.z*operand.y - self.y*operand.x)

	# Dot Project
	# dp = a & b
	def __and__(self, operand):
		if(not isinstance(operand, TripleVector)):
			raise TypeError("Operand must be type TripleVector")

		return (self.x * operand.x) + \
		       (self.y * operand.y) + \
		       (self.z * operand.z)
 
	# Operations
	def normal(self):
		return self.__copy() / self.magnitude()

	def unit(self):
		return self.normal()

	def magnitude(self):
		return (self.x**2 + self.y**2 + self.z**2)**(.5)