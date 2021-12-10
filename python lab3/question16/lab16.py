#Write a Python program to remove newline characters from a file.


def a(b):

    list = open(b).readlines()

    return [s.rstrip('\n') for s in list]

print(a("second.txt"))