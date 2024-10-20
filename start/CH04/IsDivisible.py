#!/usr/bin/env python3
# Script that tells you if a number is divisible by another
# By James Malcolm 
# Date: 10/18/24


    
def is_divisible(num, div):
    return num % div == 0

num = int(input("What is the number: "))
div = int(input("What is the divisor: "))

if is_divisible(num, div):
    print(f"{num} is divisible by {div}")
else:
    print(f"{num} is NOT divisible by {div}")