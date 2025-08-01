'''Variables that are created outside of a function (as in all of the examples above) are known as global variables.

Global variables can be used by everyone, both inside of functions and outside.
Example

Create a variable outside of a function, and use it inside the function'''



x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc() 