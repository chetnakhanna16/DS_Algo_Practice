class Student:
	def __init__ (self, fname, lname):
		self.fname = fname
		self.lname = lname

s1 = Student("Ankur", "Rastogi")
s2 = Student("Chetna", "Khanna")
print(s1.fname)

s1.roll_number = 1
s1.class_number = 12
s1.section = "A"

print(s1)
print(s1.roll_number)
print(Student)


