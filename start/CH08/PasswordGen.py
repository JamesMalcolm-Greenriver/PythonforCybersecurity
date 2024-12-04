#!/usr/bin/env python3
# Script that checks passwords agains haveibeenpwned.com API
# https://haveibeenpwned.com/API/v3#PwnedPasswords
# By James Malcolm

import tkinter as tk
from tkinter import font
import random, secrets, string, hashlib, requests

r = tk.Tk()

#Password gen options
use_numbers = False
use_uppercase = False
use_symbols = False
length = 15

#Temp Vars
temp_pass = ""
success = False
string_var = tk.StringVar()

use_num = tk.BooleanVar()
use_upper = tk.BooleanVar()
use_sym = tk.BooleanVar()

#Create a password using inputs and secrets
def create_password():
    pool = string.ascii_lowercase
    if use_num.get(): 
        pool += string.digits
    if use_upper.get(): 
        pool += string.ascii_uppercase
    if use_sym.get():
        pool += string.punctuation
    
    return ''.join(secrets.choice(pool) for i in range(length))

# Creates a hash from given password
def create_hash(password):
    return hashlib.sha1(password.encode()).hexdigest()

#Generate Password Function
def gen_password():
    print("Generating Password")
    while(not success):
        #Creat the password and hash
        temp_pass = create_password()

        print(temp_pass)

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
            string_var.set("Generated Password: " + temp_pass)
            break
        else:
            continue

#Creating GUI
r.title('James\' Password Generator')
r.configure(bg='lightblue')
r.geometry("500x300")

check_font = font.Font(family="Helvetica", size=14)
label = tk.Label(r, text="Password Options")

password_label = tk.Label(r, textvariable=string_var, bg='white', width=50, font=check_font)
string_var.set("Generated Password: ")

submit_btn = tk.Button(r, text='Generate Password', width=40, command=gen_password)

check_numbers = tk.Checkbutton(r, text="Use Numbers", variable=use_num, onvalue=True, offvalue=False, font=check_font, bg='lightblue')
check_uppercase = tk.Checkbutton(r, text="Use Uppercase Letters", variable=use_upper, onvalue=True, offvalue=False, font=check_font, bg='lightblue')
check_symbols = tk.Checkbutton(r, text="Use Symbols", variable=use_sym, onvalue=True, offvalue=False, font=check_font, bg='lightblue')

check_numbers.pack()
check_uppercase.pack()
check_symbols.pack()
submit_btn.pack(pady=40)
password_label.pack()

r.mainloop()