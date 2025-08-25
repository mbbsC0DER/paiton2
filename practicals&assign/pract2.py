
# # practical 2a
# n = int (input("Enter a number to count factorial : "))
# fact =  1 
# def factorial():
#     global fact 
#     for i  in range(1 , n + 1):
#         fact *= i
#     return fact
# ans = factorial() 
# print ("The factorial of the number is" , ans )


# practical 2b
# def sum_of_all_numbers() :
#     # n1 = int (input ("Enter 1st number : "))
#     # n2 = int (input ("Enter 2nd number : "))
#     # n3 = int (input ("Enter 3rd number : "))
#     # n4 = int (input ("Enter 4th number : "))
#     n1 , n2 , n3 , n4 = map(int , input ("Enter any 4 numbers : ").split())
#     return n1 + n2 + n3 + n4
# res = sum_of_all_numbers()
# print ("The sum of all the numbers is " , res )

# practical 2c
# def largest(a,b,c): 
#     if (a > b and a > c):
#         res = a 
#     elif (b > a and b > c):
#         res = b 
#     else:
#         res = c 
#     return res 

# a = int (input ("Enter 1st number : "))
# b = int (input ("Enter 2nd number : "))
# c = int (input ("Enter 3rd number : "))
# ans = largest(a,b,c) 
# print (f"The largest among {a} , {b} , {c} is " , ans )

# practical 2d
# r = int (input ("ENter the radius : "))
# def area(r):
#     return 3.14*r *r 
# def circumference (r):
#     return 2 * 3.14 * r  
# print (f"The area of the circle of radius {r } is {area(r) } ")
# print (f"The circumference of the circle of radius {r} is {circumference(r) }")


## practical 2e
# add  = lambda x , y : x + y 
# subtract = lambda x , y : x - y
# multiply = lambda x , y : x * y
# divide = lambda x , y : x / y if y != 0 else print ("Cannot divide by zero .")

# x = float (input ("Enter x : "))
# y = float (input ("Enter y : "))

# print (f"Addition of {x} and {y} = {add(x,y)}")
# print (f"Subtraction of {x} and {y} = {subtract(x,y)}")
# print (f"Multiplication of {x} and {y} = {multiply(x,y)}")
# print (f"Division of {x} and {y} = {divide(x,y)}")