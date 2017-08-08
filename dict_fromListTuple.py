# From a list of tuples
d = dict([("age", 25)])

class Person(object):
    def __init__(self, name, profession):
        self.name = name
        self.profession = profession
 
people = [Person("Nick", "Programmer"), Person("Alice","Engineer")]
professions = dict([ (p.name, p.profession) for p in people ])
print professions

# another way to create dynamic dictionary from list of tuple
people = [Person("Nick", "Programmer"), Person("Alice","Engineer")]
professions1 = {}
for p in people:
    professions[p.name] = p.profession
print professions1