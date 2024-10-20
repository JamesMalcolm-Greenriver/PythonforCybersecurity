#!/usr/bin/env python3
# Script that writes to a file
# By James Malcolm 
# Date: 10/18/24

hack_file = open("hackme.txt", "w")

hack_file.write("Name: " + input("What is your name? ") + "\n")
hack_file.write("Favorite Color: " + input("What is your favorite color? ") + "\n")
hack_file.write("First Pet's Name: " + input("What was your first pet's name? ") + "\n")
hack_file.write("Mother's Maiden Name: " + input("What is your mother's maiden name? ") + "\n")
hack_file.write("Elementary School: " + input("What elementary school did you attend? ") + "\n")

hack_file.close()