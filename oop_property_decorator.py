class Employee:

	def __init__(self, firstName, lastName): #constructor
		# instance variables
		self.firstName = firstName
		self.lastName = lastName
		
	@property
	def email(self):
		return '{}.{}@company.com'.format(self.firstName, self.lastName)	
	
	@property
	def fullName(self):
		return '{} {}'.format(self.firstName, self.lastName)

	@fullName.setter
	def fullName(self, name):
		firstName, lastName = name.split(' ')
		self.firstName = firstName
		self.lastName = lastName

	@fullName.deleter
	def fullName(self):
		print('Delete Name')
		self.firstName = None
		self.lastName = None

	

employee1 = Employee('Patrick', 'Wang')

employee1.fullName = 'Donald Trump'

print(employee1.firstName)
print(employee1.email)
print(employee1.fullName)

del employee1.fullName
print(employee1.firstName)