import os
from task import Task
import memory as mem
import id_utils as idu
import utils as u


#Creation, Deletion, and Archival Helper Functions --------------------------------------------------------------------------------


def create_task(name: str, priority = None, tags = None): 
    #when a task is created the function should:
        # i want a new task id to be generated using the get_next_id function
        # i want a new task to be created using Task object from task.py
        # immediately be saved using save_task from mem.py
        # i want the task object returned from the function (seems important and conventional)
    if not name.strip():
        print("Task creation failed: task name cannot be empty.")
        return None
    
    if u.normalize_name(name) in mem.get_used_names():
        print("Task creation failed: task name cannot be the same as another task.")
        return None

    new_id = idu.get_next_id()
    if new_id is None:
        print(f"Task creation failed: could not generate valid ID.")
        return None
    
    new_task = Task(new_id, name, priority, tags)
        #if no priority is given, init should default it to 3
        #if no tags are given, init should default it to [] 
        #status is automatically "Ready", should not be determined by create function
        #created_at is determined by init, does not need to be included
        #the only necessary items are task id (generated) and a name (string, provided upon creation)

    mem.save_task(new_task) #store the new task using the memory file

    
    return new_task