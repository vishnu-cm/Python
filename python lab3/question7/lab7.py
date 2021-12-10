#Write a Python program to read a file line by line store it into an array.


def a(b):

        content_array = []

        with open(b) as c:
                
                for line in c:

                 content_array.append(line)
                 print(content_array)

a('two.txt')