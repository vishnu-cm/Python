#Write a Python program to write a list to a file.


a_list = ["abc", "def", "ghij"]

textfile = open("two.txt", "w")

for element in a_list:

    textfile.write(element + "\n")
    
textfile.close()
