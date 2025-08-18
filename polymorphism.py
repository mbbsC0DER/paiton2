#Run time polymorphism
class vehicle():
    def move(self):
        print ("a vehicle moves")

class car(vehicle):
    def move(self):
        print ("the car moves")

class bike (vehicle):
    def move(self):
        print ("the bike moves")

classes = [car() , bike()]
for i in classes:
    i.move()

#compile time polymorphism
class add():
    def sum(self , a , b=0 , c=0):
        return a+b+c

a = add()
print (a.sum(10))
print (a.sum(10,20))
print (a.sum(10,20,30))