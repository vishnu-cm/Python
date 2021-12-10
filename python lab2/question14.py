#Write a Python program to remove an item from a set if it is present in the set.


a = set([0, 1, 2, 3, 4, 5])

print("Set of elements:",a)

a.discard(4)

print("4 removed from the set:",a)


