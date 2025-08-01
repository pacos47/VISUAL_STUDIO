
#Create a class named Person, with firstname and lastname properties, and a printname method:
#parent


class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method:

x = Person("John", "Doe")
x.printname() 

#child

class Student(Person):    #declaration of a child:  class child(parent)
 pass 

x = Student("Mike", "Olsen")
x.printname() 
#.....................BETTER:  INITIALIZE Studend and ADD now parameters and methods

class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)           #...use PERSON'S INITIALIZATION
    self.graduationyear = year             #ADD A NEW PARAMETER

x = Student("Mike", "Olsen", 2019)      #see line 29

x.printname()       #inhereted from Person via super()
print(x.graduationyear)


