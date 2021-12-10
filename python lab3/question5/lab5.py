#Write a Python program to read a file line by line and store it into a list.


with open('two.txt') as f:

    content = f.readlines()
    li = [x.strip() for x in content]
    
print(li)