#Write a Python program to append text to a file and display the text.


f = open("two.txt", "a")

f.write("\n This program is done by python language")

f.close()

f = open("two.txt", "r")

print(f.read())