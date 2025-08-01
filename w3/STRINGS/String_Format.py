#we cannot combine strings and numbers like this:
#    Example  resulting to ERROR!
'''
age = 36
txt = "My name is John, I am " + age
print(txt)
'''

#The format() method takes the passed arguments, formats them, and places them in the string where the placeholders {} are:
pi=3.14159

age = 36
txt = "My name is John, I am  {}" 
print(txt.format(age))

#............................
quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))
#.....................................
price = 49
txt = "The price is {} dollars"
print(txt.format(price))    #49 as string
#.............................................
#Format the price to be displayed as a number with two decimals:
txt = "The price is :{:.2f} dollars"
print(txt.format(price))
#............
#Format the price to be displayed as a number with two decimals AND a WIDTH =8 meaning a TOTAL of 8 places:
#2 decimal+1 for point=3 up to here, leaving  8-3=5 places for the integral part, if any 
# for this case (49) 5-2=3 spaces will precede the number  (width must be >5 to see any spaces)
txt = "The price is :{:8.2f} dollars"
print(txt.format(price))
#..........................................
#Index Numbers

#You can use index numbers (a number inside the curly brackets {0}) to be sure the values are placed in the correct placeholders:

quantity = 3
itemno = 567
price = 49
myorder = "I want {0} pieces of item number {1} for {2:.2f} dollars!!!"   #first 2 in {2:.2} is the nr 2 item (here price)
print(myorder.format(quantity, itemno, price))
#.............................
#Also, if you want to refer to the same value more than once, use the index number:

age = 36   #age->0
name = "John"   # name->1
txt = "His name is {1}. {1} is {0} years old."
print(txt.format(age, name))     
#..........................................
#NAMED Indexes
myorder = "I have a {carname}, it is a {model}."
print(myorder.format(carname = "Ford", model = "Mustang"))
#............................................
txt = "For only {price:.2f} dollars!"
print(txt.format(price = 49))
#...............ALL IN ONE..............
print("I have a {carmake}, it is a {model}...for only {price}$!".format(carmake = "Fiat", model = "Punto",price=650))









































