import utils as u
import task_manager as tm
from task import Task

def prompt_create_task():
    name = input(f"Please enter task name: ")

    print(f"\nSelect task priority: ")
    print(f"----------------------")
    for i in range(3, -1, -1):
        print(f"[{i}] = {Task.priorities[i]}")
    priority = input(f"Enter a number 0-3: ")   

    while (not (priority.isdigit())) or (int(priority) not in range(4)):
        print("Priority must be an integer between 0 and 3.")
        print(f"\nSelect task priority: ")
        print(f"----------------------")
        for i in range(3, -1, -1):
            print(f"[{i}] = {Task.priorities[i]}")
        priority = input(f"Enter a number 0-3: ")
    
    priority = int(priority)


    tags = u.parse_tags_raw(input("Please enter tags (comma separated): "))


    task = tm.create_task(name, priority, tags)

    if task:
        print(f"\nTask \"{task.name}\" created")
        print(f"|-- ID: {task.id}")
        print(f"|-- Priority: {Task.priorities[task.priority]}") 
        print(f"|-- Status: {Task.priorities[task.status]}")
    
        if task.tags:
            print(f"|-- Tags: {', '.join(task.tags)}")
        else:
            print(f"|-- Tags: None")
        #update later to suggest the top three most common tags (alphabetically if tags have the same number of uses)
    else:
        print(f"\nTask creation failed.")

    
