
   #x = "awesome"
global x 
x= "blabla"
def myfunc():
  global x
  x = "fantastic"

print("x=...",x)

myfunc()

print("x=!!! " + x) 