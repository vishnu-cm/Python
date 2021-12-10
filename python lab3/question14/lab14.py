#Write a Python program to combine each line from first file with the corresponding line in second file.


with open('first.txt') as a, open('second.txt') as b:

    for line1, line2 in zip(a, b):

        print(line1+line2)
		