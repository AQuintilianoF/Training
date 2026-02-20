import json
import os

json_file = "planner\schedule.json"

def save(new_event):

    if os.path.exists(json_file):
        
        with open(json_file, "r") as f:
            events = json.load(f)
    else:
        events = []

    new_id = max((event["id"] for event in events), default=0) +1


    new_event['id'] = int(new_id)

    events.append(new_event)

    with open(json_file, 'w') as f:
        json.dump(events, f, indent = 2)
            
    return True

def load():

    if os.path.exists(json_file):

        with open(json_file, "r") as f:
            events = json.load(f)
    else:
        events = []

    return events

def remove(delete_id):

    deleted = False
    delete_id = int(delete_id)
    if os.path.exists(json_file):

        with open(json_file, "r") as f:
            events = json.load(f)
    else:
        return False

    for i, e in enumerate(events):
        test = int(e['id'])
        if test == delete_id:
            del events[i]
            deleted = True
            break

    with open(json_file, 'w') as f:
        json.dump(events, f, indent = 2)


    return deleted
