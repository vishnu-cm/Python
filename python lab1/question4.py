#Create a program that asks the user for a number and then prints out a list of all the divisors of that number.

number = int(input("Enter a number:"))

divisors = [a for a in range(1, number+1) if number % a == 0]

print("Divisor(s):",divisors)