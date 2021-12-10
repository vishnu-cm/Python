#Write a python program to find the longest words.


def a(b):

    with open(b, 'r') as infile:

        words = infile.read().split()

    max_len = len(max(words, key=len))

    return [word for word in words if len(word) == max_len]
 
print(a('two.txt'))