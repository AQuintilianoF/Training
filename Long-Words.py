import os
from re import split 

print ('\n\t\t\33[32m Count Long Words \33[0m\n\n ')

string = input ('Enter text that will be analysed - ')
words = string.split()
long_words = []


for word in words:
    count = len(word)
    if count > 10:
        long_words.append(word)

if not long_words:
    print(' \n\nNo word found in the text ')

for i in long_words:
    print (i)

os.system('pause')
os.system('cls')