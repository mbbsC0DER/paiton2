class mammal():
    def base(self):
        print ("mammals have breasts ")

class animal (mammal):
    def child1(self):
        print ("all animals are not mammals")
#Single 
a = animal()
a.base()
a.child1()

class dog (animal):
    pass
#multilevel
d=dog()
d.base()
d.child1()

class cute():
    def pooki(self):
        print ("they are cute")

class cat(animal , cute):
    pass

#multiple
c=cat()
c.child1()
c.pooki()

#hierarchial
c.child1()
d.child1()

#hybrid
c.base()
c.pooki()