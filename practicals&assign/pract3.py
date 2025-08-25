# str = input ("Type your string : ")
# vowels = "aeiouAEIOU"
# vcount = 0
# ccount = 0
# for c in str :
#     if c.isalpha() :
#         if c in vowels :
#             vcount += 1 
#         else :
#             ccount += 1
#     # else:
#     #     print ("Enter valid string .")
#     #     break 
# print (f"Number of vowels in {str} is {vcount}")
# print (f"Number of consonants in {str} is {ccount}")

# str = "2024 was a leap year"
# sep = input ()
# print (str.split(sep))
# def calculator():
#     print("Simple Calculator")
#     print("Options: add, subtract, multiply, divide")
#     operation = input("Enter operation: ").strip().lower()
#     a = float(input("Enter first number: "))
#     b = float(input("Enter second number: "))
#     if operation == 'add':
#         print(f"Result: {a + b}")
#     elif operation == 'subtract':
#         print(f"Result: {a - b}")
#     elif operation == 'multiply':
#         print(f"Result: {a * b}")
#     elif operation == 'divide':
#         if b == 0:
#             print("Error: Division by zero.")
#         else:
#             print(f"Result: {a / b}")
#     else:
#         print("Unknown operation.")
# calculator()
# def factorial(n):
#     result = 1
#     for i in range(1, n + 1):
#         result *= i
#     return result

# def reverse_factorial(n):
#     for i in range(n, 0, -1):
#         print(f"{i}! = {factorial(i)}")
# n = int (input ("Enter a number : "))
# reverse_factorial(n)  # Replace 5 with any integer n
# import numpy as np
# import matplotlib.pyplot as plt
# from mpl_toolkits.mplot3d import Axes3D

# # Example: 3D surface plot
# x = np.linspace(-5, 5, 100)
# y = np.linspace(-5, 5, 100)
# x, y = np.meshgrid(x, y)
# z = np.sin(np.sqrt(x**2 + y**2))  # Example function

# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')
# ax.plot_surface(x, y, z, cmap='viridis')
# ax.set_title('3D Surface Plot')
# plt.show()
