#Write a Python program to get days between two dates. Go to the editor 
#Exampe: days between 28/02/2000 and  28/02/2001


from datetime import date

first = date(2000, 2, 28)

second = date(2001, 2, 28)

a = second - first

print(a.days)