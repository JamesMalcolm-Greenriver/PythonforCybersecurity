#!/usr/bin/env python3
# Script that checks passwords agains haveibeenpwned.com API
# https://haveibeenpwned.com/API/v3#PwnedPasswords
# By James Malcolm

import random, string, secrets, hashlib, requests

numbers = False
up = False
symbols = False
length = 15

success = False

temp_pass = ""

#Create a password using inputs and secrets
def create_password():
    pool = string.ascii_lowercase
    if numbers: 
        pool += string.digits
    if up: 
        pool += string.ascii_uppercase
    if symbols:
        pool += string.punctuation
    
    return ''.join(secrets.choice(pool) for i in range(length))

# Creates a hash from given password
def create_hash(password):
    return hashlib.sha1(password.encode()).hexdigest()

while(not success):
    #Get user inputs
    length = int(input("How long should the password be: "))
    print("Please answer the following questions with a \"Y\" or \"N\":")
    numbers = input("Include numbers: ").lower() == 'y'
    up = input("Include uppercase characters: ").lower() == 'y'
    symbols = input("Include symbols: ").lower() == 'y'
    

    #Creat the password and hash
    temp_pass = create_password()


    hash = str(create_hash(temp_pass))


    #Call the Have I Been Pwned API
    url = "https://api.pwnedpasswords.com/range/" + hash[:5]
    response = requests.get(url=url).content.decode('utf-8')
    
    resp_hashes = response.split('\r\n')
    
    found = False
    
    hash = hash.upper()
    
    for resp_hash in resp_hashes:
        tmp = resp_hash.split(":")
        if tmp[0] == hash[5:]:
            print("Password is not unique. Restarting process.")
            found = True
            break
    
    if not found:
        break
    else:
        continue

print("Your unique generated password is: " + temp_pass)
    