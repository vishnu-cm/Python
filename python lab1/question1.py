#Write a program that asks the user to enter their name and their age.Print out a message that greets them and that tells them the year that they will turn 100 years old.

name = input("Enter your name: ")

age = int (input("Enter your age: "))

user_age = (100 - age) + 2021

print ("Greetings Mr/Mrs",name, "your age is",age,"and you will turn 100 in", user_age)