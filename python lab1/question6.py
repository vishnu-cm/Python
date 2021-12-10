#Ask the user for a string and print out whether this string is a palindrome or not

a = input(("Enter a string: "))

if(a == a[::-1]):

    print("The string is a palindrome")
else:
    print("The string is not a palindrome")