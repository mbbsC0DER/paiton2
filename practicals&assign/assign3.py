"""1. Write a program to read a text file and print all unique words in sorted order."""

with open("file1.txt" , "r") as f:
    content = f.read()
    li = content.split()
    seq = sorted(set(li))
    print (seq)

"""2. Write a program that opens a file, reads its contents, and ensures that the file is closed properly using a finally block."""

try :
    f1 = open("file1.txt" , "r")
    print (f1.read())
except FileNotFoundError :
    print ("The file is not available .")
finally :
    print ("Closing the file (if opened)")
    try :
        f1.close()
    except:
        pass

"""3. Create a class Quiz that stores multiple-choice questions in a list. Method to display a
question, accept an answer, and calculate the score."""

import random
class quiz:
    def __init__(s):
        s.point = 0
        s.question = [("What is the capital of India?", "B") , ("Which animal's milk never curdles?" , "C") , ("Which element is present in heavy water?" , "B") , ("Which of the following is an input device?", "C")]
        s.option = [["A) Mumbai" , "B) Delhi" , "C) Kolkata", "D) Chennai"] , 
              ["A) Cow" , "B) Buffalo" , "C) Camel ", "D) Goat"] ,
              ["A) Heavy Oxygen","B) Heavy Hydrogen","C) Heavy Chlorine","D) Heavy Nitrogen"] ,
              ["A) Printer","B) Monitor","C) Keyboard", "D) Speaker"]]
    def display(s):
        q_rand = random.randint(0,3)
        a , b = s.question[q_rand]
        print (a)
        for i in s.option[q_rand]:
            print (i)
        ans = input ("Enter correct option : ").upper()
        if ans == b :
            print ("Correct answer ! \t 1 point added ")
            s.point += 1
        else :
            print ("Wrong answer .")

    def dis_point(s):
        print (f"You have {s.point}points .")

a = quiz()
print ("\t QUIZ GAME")
inp=1
while inp!=3 :
    print ("1.Start\n2.Check Points\n3.Exit\n")
    inp = int (input("Enter task : "))
    if inp == 1 :
        a.display()
    elif inp == 2 :
        a.dis_point()
    else :
        print ("THANK YOU")
        break




