#Write a Python program to get the file size of a plain file


import os
 
file_size = os.path.getsize('two.txt')

print("File Size is :", file_size, "bytes")