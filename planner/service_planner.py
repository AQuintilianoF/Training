from datetime import datetime, timezone, time, timedelta
import json_resp as j
import os


def add_task( date, time, text):


    task_list = {'id':0,'Date':date,'Time':time,'Text':text}

    bool = j.save(task_list)

    if not bool:
        return False

    return True

def load_task():

    list_task = j.load()
    return list_task

def remove_task(id):

    bool = is_int(id)

    if not bool:
        return False
    bool = j.remove(id)

    return bool

def is_int(value : str) -> bool:
    try:
        int(value)
        return True
    
    except ValueError:
        return False
    
