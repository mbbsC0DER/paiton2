"""age = int (input("Enter your age : "))

if age < 13 :
    print ("CHILD")
elif age <= 19 :
    print ("TEENAGER")
elif age < 60:
    print ("ADULT")
else :
    print ("SENIOR")

age = 7
day = "Wed"

price = 12 if age >= 18 else 8
if day == "Wed" :
    price -= 2

print (f"Ticket price for you is {price}")

marks = 87

if marks <100 and marks >0 :
    if marks >= 90:
        print ("A grade ")
    elif marks >= 80 :
        print ("B grade ")
    elif marks >= 70 :
        print ("C grade ")
    elif marks >=60 :
        print ("D grade ")
    else :
        print ("E grade")
else :
    print ("Give valid marks .")
"""
"""
fruit = "apple"
color = "green"
if fruit = "banana":
    if color == "green":
        print(f"Your {fruit} is unripe")
    elif color == "yellow":
        print (f"Your {fruit} is ripe")
    elif color == "brwon" :
        print (f"Your {fruit} is overripe .")
else :
    print ("we dont have info regarding this fruit")


weather = input ("enter weather")
if weather.lower() =="sunny" :
    print ("GO for a walk")
elif weather.lower() == "rainy" :
    print ("read a book")
elif weather.lower() == "snowy":
    print ("build a snowman")


dist = int (input ("enter the distance you want to travel : "))
if dist < 3 :
    mode = "walking"
elif dist < 15 :
    mode = "bike"
else :
    mode = "car"
print (f"You can go by {mode}")    


password = input ("ENtr your password : ")
chars = len(password)
if chars < 6 :
    print ("too weak !")
elif chars <= 10 :
    print ("thats medium .")
else :
    print ("damn thats strong ,")


year = int (input("enter year : "))
if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0 ):
    print (f"{year} is a leap year .")
else :
    print (" not a leap year .")
"""
