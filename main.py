import string
import secrets

letters = string.ascii_letters
digits = string.digits
special_chars = string.punctuation

bank =  letters + digits + special_chars 

pwd_length = 12

while True:
    pwd = ''
    for i in range(pwd_length):
        pwd += ''.join(secrets.choice(bank))

    if (any(char in special_chars for char in pwd) and sum(char in digits for char in pwd)>=2):
        break

print(pwd)
