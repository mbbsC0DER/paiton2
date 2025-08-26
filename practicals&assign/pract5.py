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
key = ["name", "age", "gender" ]
value = ["John", 25, "Male"]
dict = {}
for i in range(min(len(key) , len(value))) :
    dict[key[i]] = value[i] 
# for k , v in zip(key , value):
#     dict[k] = v
print (dict)

"""Q4) Write a program to sort a dictionary by its values."""

"""Q5) Given a dictionary of products and prices, write a program to display
products costing more than ₹100."""
dict = {"shampoo" : 75 , "dryer" : 110 , "books" : 200}
for i in dict :
    if dict[i] >  100 :
        print (dict[i])
    else :
        pass


