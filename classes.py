class Person:
    color = "Red"

clr = Person.color

print(clr)

newPerson = Person
newPerson.color = "Green"

print(Person.color)
