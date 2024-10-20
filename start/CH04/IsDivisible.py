#!/usr/bin/env python3
# Script that tells you if a number is divisible by another
# By James Malcolm 10/12/24

num = int(input("What is the number: "))
divisor = int(input("What is the divisor: "))

if num % divisor == 0:
    print(f"{num} is divisible by {divisor}")
else:
    print(f"{num} is NOT divisible by {divisor}")