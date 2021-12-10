"""
I have a folder with different files in it of different file names. Eg: A pthon web.html, continue Statement.txt, History of python.txt, image.png, Python File Handling.txt 
The files can have any content. So you can create any files you like.
Write a python program to get all the filenames of the files and print them in an ascending order.
"""

import os
 
path = "C:/Users/Max/Desktop/Lab/Python/python lab5/question1"

dir_list = os.listdir(path)
 
print("Files and directories in '", path, "' :")
 
print(dir_list)