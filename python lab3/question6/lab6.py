#Write a Python program to read a file line by line store it into a variable


def a(b):

    with open (b, "r") as c:
     data = c.readlines()
                
     print(data)

a('two.txt')

