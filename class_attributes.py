# import math
# class circle():
#     def __init__(self , r):
#         self.r = r 
#     def area(self):
#         return math.pi * self.r**2
#     def circum(self):
#         return 2 * math.pi * self.r
# c1 = circle(10)
# print (f"the area of the circle is {c1.area()}")
# print (f"THe circumference of the circle is {c1.circum()}")
class base ():
    "this is a docstring"
    v = 5
    def __init__(self , value ):
        self.value = value 
    def val(self):
        print (f"The value is {self.value}")

print (base.__doc__)
print (base.__name__)
print (base.__module__)
print (base.__dict__)
print (base.__bases__)