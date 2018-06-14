from enum import Enum

class People(Enum):
	PATRICKWANG = 0
	LUCYWANG = 1

class Person(object):

	def factory(type):
		if type == People.PATRICKWANG:
			return PatrickWang()
		if type == People.LUCYWANG:
			return LucyWang()
		raise AssertionError("Bad Name: " + type)

	factory = staticmethod(factory)


class PatrickWang(Person):
	def name(self):
		return "Patrick Wang"


class LucyWang(Person):
	def name(self):
		return "Lucy Wang"

def main():
	obj1 = Person.factory(People.PATRICKWANG)
	obj2 = Person.factory(People.LUCYWANG)

	print(obj1.name())
	print(obj2.name())


if __name__ == '__main__':
    main()