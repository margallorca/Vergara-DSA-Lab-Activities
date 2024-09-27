# *************************************************************
# Lab Exercise 3: Diamond Shape                               *
# Programmed By: MARGARETTE VERGARA                           *
# Date Submitted: September 27, 2024                          *
# *************************************************************

def print_diamond(n):
    if n % 2 == 0:
        print('Please provide an odd integer.')
        return
    for i in range(1, n+1, 2):
        print(' '*(n//2 - i//2) + '*'*i)
    for i in range(n-2, 0, -2):
        print(' '*(n//2 - i//2) + '*'*i)


n = int(input('Enter an odd number: '))
print_diamond(n)
