#Write a Python program to count the number of lines in a text file.


with open(r"two.txt", 'r') as a:

    x = len(a.readlines())
    
    print('Total lines:', x)