"""Q1) Write a program to input a 3x3 matrix from the user (as a list of lists).
• Find the transpose of the matrix.
• Calculate the sum of each row and each column."""

matrix = [] 
for i in range(3):
    for j in range(3) :
        matrix[i][j] = int(input(f"Enter no. for row {i} and coloumn {j} :"))
    pass

print (matrix)
for i in range(3):
    for j in range(3):
        print (matrix[i][j] , end = " ")
    print ()

