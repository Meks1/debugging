# Mērķis: 
# uzģenerēt paroli no burtiem un cipariem noteiktā garumā
import random
import string

password_length = input("Kāds būs garums?")

password = ""
for i in range(int(password_length)):
    if i % 2 == 0:
        password += str(random.randint(0, 9))
    else:
        password += random.choice(string.ascii_letters)

print("Jauna parole:", password)

# Kādas kļūdas izdevies atrast?
# syntax error
#no random input
# no string import
# incorrect range(must be password_length)
