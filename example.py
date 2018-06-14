#For two group of people.  They all have different ages, heights and weights and hobbies.  
#Group A is female, group B is male.  Find people from group A who has the same hobby and 
#is the same age of Group B and print out their heights and weights.  Would like to see the 
#OOP concepts are used appropriately.

class Person:
	
	def __init__(self, name, age, height, weight, hobbies):
		self.name = name
		self.age = age
		self.height = height
		self.weight = weight
		self.hobbies = hobbies

class GroupA(Person):
	def __init__(self, name, age, height, weight, hobbies):
		super().__init__(name, age, height, weight, hobbies)
		self.gender = 'Female'

class GroupB(Person):
	def __init__(self, name, age, height, weight, hobbies):
		super().__init__(name, age, height, weight, hobbies)
		self.gender = 'Male'



def main():
	male1 = GroupB('Patrick',21,160,160,'swimming')
	male2 = GroupB('James',30,170,180,'sleep')
	male3 = GroupB('John',25,170,180,'running')


	female1 = GroupA('Lucy',21,100,100,'swimming')
	female2 = GroupA('Michelle',25,110,90,'running')
	female3 = GroupA('Jane',21,120,100,'swimming')

	groupB = [male1,male2,male3]
	groupA = [female1,female2,female3]
	
	for male in groupB:
		res =[]
		for female in groupA:
			if male.age == female.age and male.hobbies == female.hobbies:
				if male not in res:
					res.append(male)
				if female not in res:
					res.append(female)

		for people in res:
			print ('name:{} height:{} weight:{}'.format(people.name, people.height, people.weight))
		if res:
			print('-----------------------------------------------------------------------')


if __name__ == '__main__':
    main()