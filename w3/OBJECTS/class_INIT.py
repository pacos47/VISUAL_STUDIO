#All classes have a function called __init__(), which is always executed when the class is being initiated.
#In the first example init is not explicity declared




#....................__inti()__  is declared

class Person :  #capital P

  def __init__(self, foo, bar):
    self.biz = foo
    self.bez = bar

p1 = Person(88, 3.14)

print(p1.bez)
print(p1.biz)
#........................METHOD...............
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.myfunc() 





















