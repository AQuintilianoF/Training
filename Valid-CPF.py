
import os

def headlinegreen(h1):
    print(f'\n\n\t\t\033[32m{h1}\033[0m')


while True:
    headlinegreen('Valid CPF')

    cpf = input('Enter your CPF (only numbers): ')


    if not cpf.isdigit():
        os.system('cls')
        print("CPF Invalid just numbers")
        continue
    elif len(cpf) != 11:
        os.system('cls')
        print("CPF Invalid it needs to be 11 chars")
        continue

    digits = list(map(int, cpf))


    soma = 0
    peso = 10
    for i in range(9):
        soma += digits[i] * peso
        peso -= 1

    dig1 = (soma * 10) % 11
    if dig1 == 10:
        dig1 = 0


    soma = 0
    peso = 11
    for i in range(10):
        soma += digits[i] * peso
        peso -= 1

    dig2 = (soma * 10) % 11
    if dig2 == 10:
        dig2 = 0


    if digits[9] == dig1 and digits[10] == dig2:
        print("CPF Valid")
    else:
        print("CPF Invalid")

    exit = int(input('Enter 1 to check another CPF or 0 to exit'))

    if exit != 1 :
        os.system('cls')
        break
    else:
        os.system('cls')
        continue

               


