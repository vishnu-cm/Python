import datetime
import os

path = "C:/Users/Max/Desktop/Lab/Python/python lab5/question2/New folder"

list = os.listdir(path)

a = str(list)

lang=["jan","feb"]
 
#print("Files and directories in '", path, "' :")

for x in lang:
    for y in list:
     print(x,y)


 

#provide month number
"""month_num = "2"
datetime_object = datetime.datetime.strptime(month_num, "%m")

month_name = datetime_object.strftime("%b")
print(month_name,dir_list)
"""
