#!/usr/bin/env python3
# Script that performs a dictionary attack against known password hashes
# Needs a dictionary file, suggested to use https://github.com/danielmiessler/SecLists/tree/master/Passwords/Common-Credentials
# By James Malcolm
# Date: 11/2/2024

from passlib.hash import sha512_crypt

ShadowFile = "C:/School/Fall2024/IT102 - Scripting/Python/Repo/PythonforCybersecurity/start/CH06/shadow"

PasswordFile = "C:/School/Fall2024/IT102 - Scripting/Python/Repo/PythonforCybersecurity/start/CH06/top10000.txt"

def test_password():
    return False
    
    
def guess_password(ShadowFile, PasswordFile):
    correct = []
    
    with open(ShadowFile, 'r') as sfile, open(PasswordFile, 'r') as pfile:
        shadows = sfile.readlines()
        passwords = pfile.readlines()
        
        for shadow in shadows:
            con = shadow.split(':')
            if len(con) < 2 or '!' in con[1] or '*' in con[1]:
                continue
            
            user, hpass = con[0], con[1].strip()
            
            for password in passwords:
                password = password.strip()
                
                print(f"Trying password for {user}: {password}")

                try:
                    if sha512_crypt.verify(password, hpass):
                        correct.append((user, hpass))
                        print(f"Found, {user}: {password}")
                except ValueError:
                    continue

guess_password(ShadowFile, PasswordFile)