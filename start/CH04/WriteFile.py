#!/usr/bin/env python3
# Script that writes to a file
# By James Malcolm 10/12/24

hack_file = open("hackme.txt", "w")

hack_file.write(input("What is your name? ") + "\n")
hack_file.write(input("What is your favorite color? ") + "\n")
hack_file.write(input("What was your first pet's name? ") + "\n")
hack_file.write(input("What is your mother's maiden name? ") + "\n")
hack_file.write(input("What elementary school did you attend? ") + "\n")

hack_file.close()