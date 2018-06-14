
class Employee:

	num_of_employee = 0
	raise_amount =1.04 #class variable

	def __init__(self, firstName, lastName, pay): #constructor
		# instance variables
		self.firstName = firstName
		self.lastName = lastName
		self.pay = pay
		self.email = firstName + '.' + lastName + '@company.com'

		Employee.num_of_employee += 1

	def getFullName(self):
		return '{} {}'.format(self.firstName, self.lastName)

	def apply_raise(self):
		self.pay = int(self.pay * self.raise_amount)

	@classmethod
	def set_raise_amt(cls, amount):
		cls.raise_amount = amount

	@classmethod #alternative constructor
	def from_string(cls, employee_str):
		firstName, lastName, pay = employee_str.split('-')
		return cls(firstName, lastName, pay)
	
	@staticmethod #use static methods when you dont access the instance or class
	def is_workday(day):
		if day.weekday() == 5 or day.weekday() == 6: #saturday and sunday
			return False
		return True

employee1 = Employee('Patrick', 'Wang', 5000)
employee2 = Employee('Test','User', 4000 )

import datetime
my_date = datetime.date(2018, 6, 12)


print(employee1.num_of_employee)
print(employee2.num_of_employee)
