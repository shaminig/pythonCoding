import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
print("Welcome to password generator")
no_letters=int(input("enter the no of letters you want  "))
no_numbers=int(input("enter the no of numbers you want  "))
no_symbols=int(input("enter the no of symbols you want  "))
password = " "
for i in range(1,no_letters+1):
    password += random.choice(letters)
# print(password)
for i in range(1,no_numbers+1):
    password += random.choice(numbers)
# print(password)
for i in range(1,no_symbols+1):
    password += random.choice(symbols)
print(password)