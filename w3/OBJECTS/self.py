#The self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class.

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.myfunc() 


#It does not have to be named self , you can call it whatever you like, but it has to be the first parameter of any function in the class:
#Example

#Use the words mysillyobject and abc instead of self:

class persona:
  def __init__(mysillyobject, name, age):
    mysillyobject.onoma = name
    mysillyobject.ilikia = age

  def myfunc(abc):
    print("Hello my name is " + abc.onoma)

p1 = persona("Ασπασια", 76)
p1.myfunc()  