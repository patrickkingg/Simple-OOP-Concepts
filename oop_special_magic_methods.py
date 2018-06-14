class Employee:

	raise_amount =1.04 #class variable

	def __init__(self, firstName, lastName, pay): #constructor (dunder = __ __)
		# instance variables
		self.firstName = firstName
		self.lastName = lastName
		self.pay = pay
		self.email = firstName + '.' + lastName + '@company.com'


	def getFullName(self):
		return '{} {}'.format(self.firstName, self.lastName)

	def apply_raise(self):
		self.pay = int(self.pay * self.raise_amount)

	def __repr__(self): #unambiguous representation of the object used for debuggin
		return "Employee('{}', '{}', {})".format(self.firstName, self.lastName, self.pay)

	def __str__(self): #make object readable used to display object data to end user
		return '{} - {}'.format(self.getFullName(), self.email)

	def __add__(self, other): #add the pay of two employees
		return self.pay + other.pay

	def __len__(self): #returnt he num of characters in the full name
		return len(self.getFullName()) 

employee1 = Employee('Patrick', 'Wang', 5000)
employee2 = Employee('Test','User', 4000 )

# print(len(employee1))
print(employee1+employee2)


# print(employee1)

# print(repr(employee1))
# print(str(employee1))

# print(employee1.__repr__())
# print(employee1.__str__())

