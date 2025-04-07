import os
from task import Task
import memory as mem


#ID Related Helper Functions ------------------------------------------------------------------------------------------------------

def get_next_id(filepath = "fern/data/last_id.txt"):
    os.makedirs(os.path.dirname(filepath), exist_ok = True) #checks for the directory (not the file) and creates it if it doesn't exist.
    try:
        with open(filepath, "r") as f:
            last_id = f.read().strip()
        if last_id == "":
            print(f"{filepath} file empty; IDs will now begin at 1.")
            last_id = 0
        elif not last_id.isdigit():
            print(f"Cannot generate new task ID; {filepath} does not contain a readable ID.")
            return None
        else:
            last_id = int(last_id)
    except FileNotFoundError:
        print(f"{filepath} file not found; generating new file. IDs will now begin at 1.")
        last_id = 0
    except OSError as e: #Problem with file i/o such as file permissions denied
        print(f"Cannot generate new task ID; error opening {filepath}: {e}")
        return None

    next_id = last_id + 1
    try:
        with open(filepath, "w") as f:
            f.write(str(next_id))
    except OSError as e:
        print(f"Error creating/writing to {filepath}: {e}")
    

    return next_id




def reset_ids(filepath = "fern/data/last_id.txt"):
    confirm = input(f"Are you sure you want to delete {filepath} and reset new task ID's to 1? (y/n)\n")
    if confirm.lower() != "y":
        print("Reset cancelled.")
        return
    else:
        confirm2 = input(f"Type \"y\" again to confirm the deletion of {filepath} (y/n)\n")
        if confirm2.lower() != "y":
            print("Reset cancelled")
            return
        else:
            try:
                os.remove(filepath)
                print("File deletion successful.")
            except FileNotFoundError:
                print("File does not exist at specified path.")
            except Exception as e:
                print(f"Error occurred during file deletion: {e}")



#Creation, Deletion, and Archival Helper Functions --------------------------------------------------------------------------------


def create_task(name, priority = None, tags = None, ):
    #temp func
    return