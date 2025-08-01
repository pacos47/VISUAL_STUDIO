#.......just declare it for later use
class foo :
    pass

foo1=foo
foo1.x=3.14159
print(foo1.x)
#.................
class bar :
    x=53

print(bar.x) 
bar1=bar
bar1.w=-7.9
print(bar1.w)   




class person :
    Name="Ben"
    Age=0

#foo=person.Name="Pacos"
foo=person
foo.nome="Pacos"
bar=person.Age=75
print(foo.Name)
print(foo.nome)

print(bar)