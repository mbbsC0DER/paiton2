'''Q1) Write a Python program that takes a list of integers as input. The program
should then:
• Remove all duplicate elements from the list.
• Sort the list in descending order.
• Find and print the second largest element in the modified list.
• Example Input: [10, 5, 20, 10, 30, 5, 20]
• Expected Output: (After removing duplicates and sorting) [30, 20, 10, 5],
Second largest: 20'''
li = [10, 5, 20, 10, 30, 5, 20]
li1 = []
for i in li :
    if i not in li1:
        li1.append(i)
    else :
        pass
print (li1)
li1.sort()
li1.reverse()
print (li1)
if len(li1) >= 2 :
    print (li1[1])
else :
    print ("No second largest element .")

'''Q2) Given two lists of numbers, list_A and list_B. Write a one-line Python code
using list comprehension to create a new list common_multiples that contains
only the numbers that are present in both list_A and list_B, and are also
multiples of 3.
1. Example Input:
• list_A = [1, 2, 3, 4, 5, 6, 9, 12]
• list_B = [3, 6, 9, 10, 12, 15]
2. Expected Output: [3, 6, 9, 12]'''

li1 = [1, 2, 3, 4, 5, 6, 9, 12]
li2 = [3, 6, 9, 10, 12, 15]
common = [x for x in li1 if x in li2 and x%3 == 0 ]
print (common)

"""Q3) Write a Python program to calculate the product of elements of the list
using def keyword."""

li = [1, 2, 3, 4 , 5]

def prod(n):
    multi = 1
    for i in n:
        multi *= i 
    return multi

print (prod(li))

"""Q4) Write a Python function get_stats(numbers) that takes a list of numbers as
input. This function should return a tuple containing three values: the
minimum number, the maximum number, and the average of all numbers in
the list.

Example Input: [10, 20, 30, 40, 50]
Expected Output: (10, 50, 30.0)"""

li = [10, 20 , 30 , 40 , 50 ]

def get_stats(n):
    n1 = min(n)
    n2 = max(n)
    avg = 0
    for i in n :
        avg += i
    avg /= len(n)
    return (n1,n2,avg)

print (get_stats(li))

"""Q5) Demonstrate how tuple assignment can be used to swap the values of two
variables in a single line of code without using a temporary variable. Provide a
code example."""
tup = (10 , 20 )
a , b = tup 
tup1 = (b , a)
print (f"Before swapping : {tup} \nAfter swapping : {tup1}")