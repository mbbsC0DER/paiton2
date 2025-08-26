'''Q1) Write a Python program to count the frequency of each character in a given string using a dictionary.'''

str = "hello my name is pratham"
dict = {}
for i in str :
    dict[i] = str.count(i)
print (dict)


"""Q2) Create a phonebook using a dictionary where names are keys and phone numbers are values. Allow the user to:
• Search for a number by name
• Add a new contact
• Delete a contact"""

phonebook = { "Pratham" : 1234567890 , "Tara" : 9087654321 , "Kripal" : 3873987432}

print (phonebook["Pratham"])
phonebook["Esha"] =  1122334455
phonebook.pop("Pratham")
print (phonebook)


"""Q3) Convert two lists into a dictionary.
• Example: keys = ["name", "age", "gender"], values = ["John", 25, "Male"]"""

# key = [1,2,3,4]
# value = ['a' , 'b' , 'c' , 'd']
key = ["name", "age", "gender"]
value = ["John", 25, "Male"]
dict = {}
for i in key :
    dict[i] = None
i = 1
for j in value :
    dict[i] = j
    i += 1 

print (dict)
