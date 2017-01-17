class Person(object):
	"""docstring for ClassName"""
	numofpple = 0
	def __init__(self, name="name", dob="11/11/11", gender="M", nationality="Kenyan"):
		self._name = name
		self._dob = dob
		self._gender = gender
		self._nationality = nationality

	def display(self):
		return "Implement at inherited level"

		
class Student(Person):
	def __init__(self, stdid, course, name, dob, gender, nationality):
		Person.__init__(self,name, dob, gender, nationality)
		self.__stdid = stdid
		self.__course = course

	def display(self):
		print [self.__stdid, self._name, self._dob, self._gender, self._nationality, self.__course ]
		
		

class Staff(Person):
	def __init__(self, staffid, category,name, dob, gender, nationality):
		Person.__init__(self, name, dob, gender, nationality)
		self.__staffid = staffid
		self.__category = category

	def display(self):
		print [self.__staffid, self.__category, self._nationality, self._dob, self._gender]
