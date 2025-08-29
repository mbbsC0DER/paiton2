"""1. Write a program that uses the math module to: Calculate the square root,
factorial, and sine of a number entered by the user."""

from math import * 
num = int (input ("ENter :"))
print ("The square root is : " , sqrt(num))
print ("The factorial is : " , factorial(num))
print ("The sine is : " , sin(num))


"""2. Use the random module to: Generate 5 random integers between 1 and 100."""

from random import *
for i in range(5):
    print (randint(0 , 100) , end = "-")


"""3. Calculate the distance between two points (x1, y1) and (x2, y2) using the
distance formula and math.sqrt()."""

x1 , y1 = (10 , 20 )
x2 , y2 = (30 , 40 )

print (sqrt ((x2 - x1)**2 + (y2 - y1)**2))


"""4. Find the Greatest Common Divisor (GCD) and Least Common Multiple (LCM) of two integers using math.gcd() and math.lcm().
"""
n1 = 10
n2 = 5 
print (gcd(n1 , n2))
# print (lcm(n1 , n2))
print (n1 * n2 // gcd(n1 , n2 ))

"""5. Generate a random password of length 8 containing letters, digits, and special characters."""

from string import * 
pswd = (ascii_letters + digits + punctuation)
# print (pswd)
p = "".join(sample(pswd ,8))
print ("PASSWORD = " , p)
# we can also do this by choice 
# "".join(choice(pswd) for _ in range(8))