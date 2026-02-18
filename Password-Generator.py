import os
import random
import string

print('\n\n\t\t\33[32m Password Generator \33[0m')

input ('Press any key to creat a Strong PassWord - ')


password_list = []

low_char = string.ascii_lowercase 
upper_char = string.ascii_uppercase
numb = string.digits
symbols = ('!','#','$','%','&','?','@')

password_list.extend(random.choices(upper_char, k=3))
password_list.extend(random.choices(numb, k=3))
password_list.extend(random.choices(low_char, k=3))
password_list.extend(random.choices(symbols, k=3)) 


random.shuffle(password_list)
password = ''.join(password_list)

print (f' Password Gereted was {password}')

os.system('pause')
os.system('cls')
