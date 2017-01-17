class Person(object):
	"""docstring for ClassName"""
	numofpple = 0
	def __init__(self, name="name", dob="11/11/11", gender="M", nationality="Kenyan"):
		self._name = name
		self._dob = dob
		self._gender = gender
		self._nationality = nationality
		
class Student(Person):
	def __init__(self, stdid, course):
		self.__stdid = stdid
		self.__course = course
		

class Staff(Person):
	def __init__(self, staffid, category="teaching"):
		self.__staffid = staffid
		self.__category = category
