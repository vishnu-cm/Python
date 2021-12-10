#Write a Python program to count the number of characters (character frequency) in a string.


from collections import Counter
  
a = input(("Enter: "))
  
b = Counter(a)
  
print ("Number of characters (character frequency) :\n " +  str(b))