"""1. Write a program to read a text file and display it line by line."""

with open("file1.txt" , "r") as f1 :
    content = f1.read()
    print (content)
   
"""2. Write a program to read a file and print only those lines that start with the letter A."""

import re
with open("file1.txt" , "+r") as f2 :
    content = f2.readlines()
    for i in content:
        # regex = r"^A"
        if re.match("A" , i):
            print (i)
        else :
            pass


"""3. Write a program to count the number of lines, words, and characters in a text file."""

with open ("file1.txt" , "r") as f3 :
    content = f3.readlines()
    lcount = wcount = ccount = 0
    for i in content :
        lcount += 1
        # wcount = len(i.split(i))
        for j in i :
            ccount += 1 
    f3.seek(0)
    words = f3.read()
    wcount = len(words.split())
    print (f"The line count is : {lcount} \nThe words count is : {wcount} \nThe character count is : {ccount}")

"""4. Write a program to copy the content of one file into another file."""

with open ("file1.txt" , "r") as f4 :
    content = f4.read()

with open ("file2.txt" ,  "w") as f4b :
    f4b.write(content)

"""5. Write a program to remove all the blank lines from a file."""

with open ("file3.txt" , "r") as f5 :
    lines = f5.readlines()
    print (lines)
    lines = [i.replace("\n" ,"") for i in lines]
with open ("file3.txt" , "w+") as f5b:
    f5b.writelines(lines)
    f5b.seek(0)
    print (f5b.read())