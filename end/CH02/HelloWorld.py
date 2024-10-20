#!/usr/bin/env python3
# A simple "Hello World" script in python
# Created by James Malcolm, 09/23/2024

# 
# print(f"Hello {input("Q: What is your name?\n")}. In 2 years you will be {int(input("Q: And how old are you?\n"))+ 2} years old! Today is going to be a great day!")

name = input("Please enter your name: ")

print(f"Hello {name}.\nToday will be a great day {name}!")

age = int(input("Please enter your age: "))

future_age = age + 2

print(f"In 2 years you will be {future_age} years old.")