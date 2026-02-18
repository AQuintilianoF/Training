import os

print('\n\t\t\33[32m Count Vowels \33[0m\n\n')

string = input('Enter complite text - ').lower()

vowels = ['a','e','i','o','u']
count_v = 0

for char in string:
    if char in vowels:
        count_v +=1
        

print(f' The number of vowels in this text is : {count_v}')

os.system('pause')
os.system('cls')