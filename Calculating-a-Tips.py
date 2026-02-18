def headlinegreen(h1):

    print(f'\033[33m{h1}\033[0m')


headlinegreen('RECEIPT')


total = float(input('Enter with total amount of the bill - '))
tip = int(input('Enter with prtcrntage of the tip - '))

result_total_tip = (total * (tip/100))
result_total = total + result_total_tip

print(f''''
    the total amount of the bill is {result_total:.2f}
        and 
    the total amount of the tips is {result_total_tip:.2f}
      ''')