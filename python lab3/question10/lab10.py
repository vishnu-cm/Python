#Write a Python program to count the frequency of words in a file.


from collections import Counter

def a(b):

        with open(b) as f:

                return Counter(f.read().split())

print("Count frequency of words in the file :",a("two.txt"))