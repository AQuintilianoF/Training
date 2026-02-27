from datetime import datetime, timezone, time, timedelta
import json_resp as j




def add_task(self):

    event_dict = {
    "Id": self.id,
    "Date": self.date,
    "Time": self.time,
    "Text": self.text,
    "Status": self.status,
                    }

    bool = j.save(event_dict)

    if not bool:
        return False

    return True

def new_id():

    id = j.new_id()

    return id

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
    
