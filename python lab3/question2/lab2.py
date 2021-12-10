#Write a Python program to read first n lines of a file.


a = open("two.txt")

number_of_lines = 3

for i in range(number_of_lines):
    line = a.readline()

print(line)

