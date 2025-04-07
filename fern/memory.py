#Task storage

import os
import json
from task import Task

def save_task(task: Task, filepath = "fern/tasks/tasks.txt"):
    os.makedirs(os.path.dirname(filepath), exist_ok = True) #checks for directory and creates it if it is absent
    try:
        with open(filepath, "a") as f:
            f.write(json.dumps(task.to_dict()) + "\n")

    #possible issues: OsError (permissions problem)
    except OSError as e:
        print(f"Error creating/writing task to file: {e}")
        return