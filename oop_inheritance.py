
class Employee:

	
	raise_amount =1.04 #class variable

	def __init__(self, firstName, lastName, pay): #constructor
		# instance variables
		self.firstName = firstName
		self.lastName = lastName
		self.pay = pay
		self.email = firstName + '.' + lastName + '@company.com'

		

	def getFullName(self):
		return '{} {}'.format(self.firstName, self.lastName)

	def apply_raise(self):
		self.pay = int(self.pay * self.raise_amount)

class Developer(Employee):
	raise_amount = 1.10

	def __init__(self, firstName, lastName, pay, prog_lang): #constructor for developer class
		super().__init__(firstName, lastName, pay) # employee is hte super class
		self.prog_lang = prog_lang

class Manager(Employee):

	def __init__(self, firstName, lastName, pay, employees=None): #set default to None
		super().__init__(firstName, lastName, pay)
		if employees is None:
			self.employees = []
		else:
			self.employees = employees

	def add_employee(self, employee):
		if employee not in self.employees:
			self.employees.append(employee)


	def remove_employee(self, employee):
		if employee in self.employees:
			self.employees.remove(employee)

	def print_employees(self):
		for employee in self.employees:
			print('-->',employee.getFullName())

dev_1 = Developer('Patrick', 'Wang', 5000, 'Python')
dev_2 = Developer('Test','User', 4000, 'Java' )

mgr_1 = Manager('Donald', 'Trump', 1, [dev_1])

# print(isinstance(mgr_1, Manager))
# print(isinstance(mgr_1, Employee))
# print(isinstance(mgr_1, Developer)) #mgr_1 is not an instance of developer
# print('-------------------------------------------------------------------------')
# print(issubclass(Developer, Employee))
# print(issubclass(Manager, Employee))
# print(issubclass(Developer, Manager))
# print(issubclass(Developer, Developer))

print(mgr_1.email)
mgr_1.add_employee(dev_2)
# mgr_1.remove_employee(dev_1)
mgr_1.print_employees()

# print(help(Developer)) help statement for visualization method resolution

# print(dev_1.email)
# print(dev_1.prog_lang)

# print(dev_1.pay)
# dev_1.apply_raise()
# print(dev_1.pay)
