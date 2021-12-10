#Write a Python program to read a random line from a file.


import random

def a(b):

    lines = open(b).read().splitlines()

    return random.choice(lines)

print(a('second.txt'))
