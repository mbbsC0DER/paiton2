"""Q1) Write a program to input a 3x3 matrix from the user (as a list of lists).
• Find the transpose of the matrix.
• Calculate the sum of each row and each column."""

# matrix = [] 
# for i in range(1,4):
#     for j in range(1,4) :
#         # print (i , j )
#         matrix[i][j] = int(input(f"Enter no. for row {i} and coloumn {j} : "))
#     pass
# print (matrix)
# for i in range(3):
#     for j in range(3):
#         print (matrix[i][j] , end = " ")
#     print ()

# matrix = []
# for i in range(3):
#     row = []
#     for j in range(3):
#         row.append(int (input("enter number : ")))
#     matrix.append(row)
# print ("The matrix looks like " ,matrix)
# tmatrix = []
# for i in range(3) :
#     col = []
#     for j in range(3):
#         col.append(matrix[j][i])
#     tmatrix.append(col)
# print ("The transpose of the matrix is : ",tmatrix)
# for i in range(3):
#     rsum = 0
#     csum = 0
#     row = []
#     col = []
#     for j in range(3):
#         rsum += matrix[i][j]
#         csum += matrix[j][i]
#     print (f"Sum of row & column {i} is {rsum}\t{csum}")    

"""Q2) You are given a list of tuples like: [("Ram", 24), ("Sham", 30), ("Amit", 20)]
• Sort the list by age.
• Then sort it by name."""
demo = [("Ram", 24), ("Sham", 30), ("Amit", 20)]
age = [b for a , b in demo ]
name = [a for a , b in demo]
# for a , b in demo :
#     age.append(b)
#     name.append(a)
print ("Before sorting : " , age , name)
age.sort()
name.sort()
print ("After sorting : " , age , name )


"""Q3) Create a dictionary student_grades where keys are student names
(strings) and values are lists of their scores (integers) in different subjects.
Write a program to:
• Add a new student and their scores.
• Update the scores for an existing student.
• Calculate and print the average score for a specific student.
• List all students who have an average score above 75.
Example Initial Dictionary: {"Alice": [85, 90, 78], "Bob": [70, 65, 80]}"""

data = {"Ankit": [95, 90, 100], "Devesh": [70, 65, 80]}
data["Pratham"] = [90,99,100]
print(data)
data["Ankit"] = [100 , 100 , 100]
print (data)
Sum = 0
for i in data["Devesh"]:
    Sum += i 
print ("The avg of deveshs marks is : " , Sum/ len(data["Devesh"]))
for i in data : 
    avg = 0
    avg = sum(data[i])/len(data[i])
    if avg > 75 :
        print (i)
    # print (data[i])

