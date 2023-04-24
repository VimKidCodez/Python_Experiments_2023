# It inherits the properties of the parent class
class parent_1:
	def __init__(self,name,age):  # This is an parent class
		self.name = name
		self.age = age
		print(name,age)

class student_1(parent_1):
	pass


t = student_1("h","32")

