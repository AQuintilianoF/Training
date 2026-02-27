import os
import sys
import service_planner as sp
import Classes as c

def ui_planner():

  print('''\033[94m
    
        ██████╗░░█████╗░██╗██╗░░░░░██╗░░░██╗  ██████╗░██╗░░░░░░█████╗░███╗░░██╗███╗░░██╗███████╗██████╗░
        ██╔══██╗██╔══██╗██║██║░░░░░╚██╗░██╔╝  ██╔══██╗██║░░░░░██╔══██╗████╗░██║████╗░██║██╔════╝██╔══██╗
        ██║░░██║███████║██║██║░░░░░░╚████╔╝░  ██████╔╝██║░░░░░███████║██╔██╗██║██╔██╗██║█████╗░░██████╔╝
        ██║░░██║██╔══██║██║██║░░░░░░░╚██╔╝░░  ██╔═══╝░██║░░░░░██╔══██║██║╚████║██║╚████║██╔══╝░░██╔══██╗
        ██████╔╝██║░░██║██║███████╗░░░██║░░░  ██║░░░░░███████╗██║░░██║██║░╚███║██║░╚███║███████╗██║░░██║
        ╚═════╝░╚═╝░░╚═╝╚═╝╚══════╝░░░╚═╝░░░  ╚═╝░░░░░╚══════╝╚═╝░░╚═╝╚═╝░░╚══╝╚═╝░░╚══╝╚══════╝╚═╝░░╚═╝

      \033[0m''')
  print ('Hello , This is your schedule...')
  print ('what are we gonna plan today??\n\n')

  while True:


    print ('''\n\t\tEnter a option below .
              1 - ADD A TASK.
              2 - SEE ALL TASKS.
              3 - DELETE A TASK.
              4 - EXIT
          ''')
    
    chosen = input('\t\t - ').strip()

    bool = sp.is_int(chosen)

    if not bool:
      print ('choice must be a integer number')
      continue

    chosen_int = int(chosen)

    if chosen_int not in range(1,5):
      print ('choice must be between 1 - 4')
      continue

    match chosen_int:
      case 1:
        print ('ADD')
        add()
      case 2:
        print ('LOAD')
        load()
        
      case 3:
        print ('DELETE')
        remove()
        
      case 4:
        print ('See you soon!!!')
        sys.exit()


    
    os.system('pause')
    os.system('cls')

def add():

  print ('Let\'s go Add a new Task')
  
  date = input('Enter date this new task (DD/MM/YYYY)   - ')
  time = input('Enter time this new task (HH:MM)(19:30) - ')
  text = input('Enter text this some for this task      - ')

  id = sp.new_id()
  event = c.Event(id,date,time,text)
  bool = sp.add_task(event)

  if not bool:
    print('Error')

  print ('Well done, that is your schedule')
  load()

def load():

  print ('Let\'s go load your schedule')
  list_load = sp.load_task()

  print("-" * 40)
  print(f'{'ID':<5}{'DATA':<15}{'TIME':<12}{'TEXT':<50}')
  print("-" * 40)
  
  for i in list_load:

    print(f'{i['Id']:<5}{i['Date']:<15}{i['Time']:<12}{i['Text']:<50}{i['Status']}')

def remove():

  print ('Are you sure ?')
  print (' nice, Let\' go Delete')

  load()

  task_delete = input('Following the list above , which ID do you wanna delete ? -')

  bool = sp.remove_task(task_delete)

  if not bool:
    print (' ID did not find , verify whethe you enter a valid number ')


  




