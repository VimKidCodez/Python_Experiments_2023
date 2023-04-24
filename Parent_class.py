
class my_class: # parent class
	def __init__(self,fname,lname):
		self.first_name = fname
		self.sfirst_name = lname
	def my_func(self):
		print(self.first_name+self.sfirst_name)

t=my_class("cat ","dome")
t.my_func()