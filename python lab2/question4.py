#Write a python program to count repeated characters in a string.


a = input(('Enter the string: '))

dictionary = {}

for char in a:
    if( char in dictionary.keys()):
        dictionary[char] += 1
    else:
        dictionary[char]=1
        
repeated = []

for char in dictionary:
    if( dictionary[char] > 1 ):
       repeated.append(char)

print(repeated)

print(len(repeated))