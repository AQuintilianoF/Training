import os 
import random



print ('''\t\33[97m
        
░██████╗░██╗░░░██╗███████╗░██████╗░██████╗  ░█████╗░  ███╗░░██╗██╗░░░██╗███╗░░░███╗██████╗░███████╗██████╗░
██╔════╝░██║░░░██║██╔════╝██╔════╝██╔════╝  ██╔══██╗  ████╗░██║██║░░░██║████╗░████║██╔══██╗██╔════╝██╔══██╗
██║░░██╗░██║░░░██║█████╗░░╚█████╗░╚█████╗░  ███████║  ██╔██╗██║██║░░░██║██╔████╔██║██████╦╝█████╗░░██████╔╝
██║░░╚██╗██║░░░██║██╔══╝░░░╚═══██╗░╚═══██╗  ██╔══██║  ██║╚████║██║░░░██║██║╚██╔╝██║██╔══██╗██╔══╝░░██╔══██╗
╚██████╔╝╚██████╔╝███████╗██████╔╝██████╔╝  ██║░░██║  ██║░╚███║╚██████╔╝██║░╚═╝░██║██████╦╝███████╗██║░░██║
░╚═════╝░░╚═════╝░╚══════╝╚═════╝░╚═════╝░  ╚═╝░░╚═╝  ╚═╝░░╚══╝░╚═════╝░╚═╝░░░░░╚═╝╚═════╝░╚══════╝╚═╝░░╚═╝
        
        \33[0m''')
def ai_numb():
        chosen_numb = random.randint(1,100)
        print(chosen_numb)
        return chosen_numb

def guess_numb():
    
    chosen_numb = ai_numb()
    while True:
    
        print('\n\t\tLet\' go to start the Game \n')
        try:
            
                guess = int(input('\t\tEnter guess number (1 - 100) -- ').strip())
                
        except ValueError:
                print ('\n\t\tIt must be a Real Number (1 - 100)')
                continue

        if  guess < 1 or guess > 100:
                print ('\n\t\tIt must be a Real Number (1 - 100)')
                continue

        
        if chosen_numb == guess:
              print('\n\n\t\t\t\033[32m You found \033[0m\n\n')

        elif chosen_numb < guess:
              print('\n\n\t\t\t\033[33m Oooh no , the number is lower  \033[0m\n\n')
              continue
        else:
              print('\n\n\t\t\t\033[33m Oooh no , the number is higher\033[0m\n\n')
              continue
      
        keep = int(input('''
                Do you wanna keep playing ?' 
                 1 - Continue' 
                 2 - Exit'
                         '''))
        if keep != 1:
              break

    

        

guess_numb()
os.system('pause')
os.system('cls')