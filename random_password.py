from random import *

letters = ['a', 'b', 'c', 'd', 'e', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
                   'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
letters_upper = [i.upper() for i in letters]
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
chars = ['*', '/', '!', '&', '^', '$']

# password_len = int(input('The length of the password = '))
password = []

pass_len = input('Enter the length of the password: ')

for letter in range(1, int(pass_len)+1):
    password.append(choice(letters))
for letter_upper in range(1, int(pass_len)+1):
    password.append(choice(letters_upper))
for number in range(1, int(pass_len)+1):
    password.append(choice(numbers))
for char in range(1, int(pass_len)+1):
    password.append(choice(chars))

shuffle(password)

password_str = ""
for char in password:
    password_str += char
    
print(password_str[:int(pass_len)])