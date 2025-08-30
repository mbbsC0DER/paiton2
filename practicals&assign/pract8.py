"""1. Create a class Student with attributes name and roll_no. , Accept data from the user and display it."""

class student:
    def __init__(s , name , roll_no):
        s.name = name 
        s.roll_no = roll_no
    def display (s):
        print (f"Name : {s.name} \nRoll no. : {s.roll_no}")
name = input ("Enter name :")
roll = int (input ("Enter roll no. : "))
s1 = student(name , roll)
s1.display()


"""2. Create a class Rectangle with attributes length and breadth. Write methods to calculate and display area and perimeter."""

class rectangle:
    def __init__(s , length , breadth ):
        s.length = length 
        s.breadth = breadth
    def area(s):
        print (f"Area of rectangle : {s.length * s.breadth}")
    def perimeter(s):
        print (f"Perimeter of rectangele : {2 * (s.length + s.breadth)}")

r1 = rectangle(7 , 12)
r1.area()
r1.perimeter()

"""3. Create a class Circle with an attribute radius. Write methods to calculate and display area and circumference using math.pi."""

from math import *
class circle :
    def __init__(s , r ):
        s.r = r
    def area(s):
        print (f"Area of circle : {pi * s.r **2}")
    def circum(s):
        print (f"Circumference of circle : {2 * pi * s.r}")
c1 = circle(12)
c1.area()
c1.circum()

"""4. Create a class Car with attributes company and model. Add a method to display car details."""

class car():
    def __init__(s , company , model):
        s.company = company
        s.model = model
    def display(s):
        print ("   Car Details")
        print("Company : " , s.company)
        print ("Model : " , s.model)
d1 = car("Tata" , "Nexon")
d2 = car ("HOnda" , "Civic")
d1.display()
d2.display()

"""5. Create a class Book with attributes title, author, and price. Accept book details from the user and display them."""

class book :
    def __init__(s , title , author , price ):
        s.title = title
        s.author = author
        s.price = price
    def display (s):
        print (f"The book {s.title} written by {s.author} is of {s.price} rupees only")

t = input("Enter title : ")
a = input ("eNTER Author :")
p = int (input("enter price :"))
b1 = book(t,a,p)
b1.display()