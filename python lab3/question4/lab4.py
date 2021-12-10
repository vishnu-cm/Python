#Write a Python program to read last n lines of a file.


a = open("two.txt", "r")

lines = a.readlines()

last_lines = lines[-4:]

print(last_lines)