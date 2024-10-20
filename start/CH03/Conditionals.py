#!/usr/bin/env python3
# example workign with conditionals
# By James Malcolm based on class lecture video
# Date: 10/18/24
    
def send_message():
    while True:
        ans = input("Is today a great day? (y/n): ".lower())
        if ans in ['y', 'n']:
            return ans
        else:
            print("Not a valid reponse, please input y or n")
            
ans = send_message()

if ans == 'y':
    for i in range(10):
        print("Yes it is.")
else:
    print("Today is not the best day.")