

from datetime import date
 
   # Static Method
#Class Method
#    Instance Method

'''If we don’t want to use class variables or instance variables, we can use static methods. 
A static method can be called without the object of the class. 
We use the decorator @staticmethod to declare a static method. This method requires neither the self nor the 
cls reference because they are not dependent on any instance or class attribute. '''

class Sample:
   
  @staticmethod
  def method():
    print('This is a static method')
 
Sample.method()

'''The class methods are bound to a class instead of the objects of the class. 
These methods can be called without the instance of the class. We can create class methods by either using the classmethod() 
method or the decorator @classmethod. 
Class methods accept cls as an argument indicating that the method points to the class instead of the object instance. '''

class Sample:
  var = "Class Variable"
 
  @classmethod
  def method(cls):
    print(cls.var)
 
Sample.method()

#Instance method

class Sample:
  def __init__(self, a):
        self.a = a
 
  def method(self):
    print(self.a)
 
obj = Sample(10)
obj.method()

#=============================================================
# random Person
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def fromBirthYear(cls, name, birthYear):
        return cls(name, date.today().year - birthYear)   #KEY : return cls(i,j) means set class Person name=, class Person age=j


    def display(self):
        print(self.name + "'s age is: " + str(self.age))

person = Person('Adam', 19)
person.display()

person1 = Person.fromBirthYear('John',  1985)
print(person1.name)
print(person1.age)
person1.display()