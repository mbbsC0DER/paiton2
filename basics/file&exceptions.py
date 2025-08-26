# import re 
# text = "this string contains text as well as 4341412 from any 1 to 9 + and (*&^%$#)"
# m = re.findall(r"\W+" , text)
# print (m)
# def div (a , b):
#     try :
#         d = a / b 
#         # num = int ("abc")
#         f= open ("data.txt" , "r")
#         content = f.read()
#     except ZeroDivisionError :
#         print ("Error . cannot divide by zero .")
#     except ValueError :
#         print ("Error , invalid conversion")
#     except FileNotFoundError :
#         print ("ERROR , file not found !")
#     else :
#         print ("Result : " , d)
#     finally :
#         print ("Execution completed !")
#         try :
#             f.close()
#         except :
#             pass
# div(5,2)
# import os 
# files = ["hello.txt" , "data.txt"]
# directory = "my_folder"
# for i in files:
#     try:
#         path = os.path.join(directory , i)
#         with open(i , "r") as f :
#             print ("Contents of , "  , i)
#             print (f.read())

#     except FileNotFoundError :
#         print (f"error :{i} not found in directory " )
    
#     finally :
#         print ("EXECUTUION COMPLETE !")

try:
    f = open("data.txt")
    data = f.readlines()
    print (data[1])
    f.close()
except FileNotFoundError :
    print ("the file is missing .")
except IndexError :
    print ("error the files has fewer lines than expected ")
finally :
    print ("Closing file , ")
    try:
        f.close()
    except:
        pass 