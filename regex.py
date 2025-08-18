import re

s = "hello i was/ born on 13th \njuly 2005"
li = ["this is a " , "this means this" , "hello everinion"]
t = "ac dabc abbaaachhs abdacsbs"
# print ( re.search('.' , s ))
# print (re.search("\." , s))
# for i in li :
#     if (re.match( r"this" , i)):
#         print ("match found ")
#     else :
#         print ("match not found ")
regex =  r"\w+"
match = re.findall(regex , s)
print (match)
