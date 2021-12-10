#Write a Python program to calculate the sum of the positive integers of n+(n-2)+(n-4)... (until n-x =< 0).


def sum_series(n):
    
    if (n-3) <= 0:
        return n
    else:
        return n + sum_series(n-3)

print(sum_series(6))

print(sum_series(7))