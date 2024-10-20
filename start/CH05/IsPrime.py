#!/usr/bin/env python3
# example workign with conditionals
# By James Malcolm
# Date: 10/20/24

def is_prime(number):
    if number > 1:        
        for i in range(2, (number//2)):
            if number % i == 0:
                return False
        return True
    else:
        return False

number = int(input("Please input a number: "))
prime = is_prime(number)

if prime:
    print(str(number) + " is prime")
else:
    print(str(number) + " is NOT prime")
        