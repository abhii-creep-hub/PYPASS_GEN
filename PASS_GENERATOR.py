import random
letter= ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm','n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M','N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers= ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols= ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/',':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~']


print("Welcome to the PyPassword Generator!")
nr_letter=int(input("How many letter would you like in your password?\n"))
nr_symbols=int(input(f"How many symbols would you like?\n"))
nr_numbers=int(input(f"How many numbers would you like?\n"))


#EASY VERSION - 4 LETTER, 2 SYMBOL, 3 NUMBER ___ fgdx$*924
#HARD VERSION - x$d24g*f9

#EASY
# password=""


# #nr_letters=4
# for char in range(1,nr_letter+1):
#     #1-4
#     random_char=random.choice(letter)
#     password+=random_char


#     print(password)

# #4 taken in each requirement s the output = 
# # p
# # pV
# # pVM
# # pVMH

# for char in range(1,nr_symbols+1):
#     password+=random.choice(symbols)

# for char in range(1,nr_numbers+1):
#     password+=random.choice(numbers)

# print(password)

#HAARDDD
password_list=[]

for char in range(1,nr_letter+1):
    
   password_list.append(random.choice(letter))

for char in range(1,nr_symbols+1):
   password_list.append(random.choice(symbols))

for char in range(1,nr_numbers+1):
    password_list.append(random.choice(numbers))

print(password_list)
random.shuffle(password_list)
print(password_list)

password=""
for char in password_list:
   password+=char
print(f"Your password is:{password}")