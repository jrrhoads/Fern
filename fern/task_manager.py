import os
from datetime import datetime


#ID Related Helper Functions ------------------------------------------------------------------------------------------------------

def get_next_id(filepath = "fern/data/last_id.txt"): 
    #this function will (assuming no OsErrors are found)
        #increment the last id from file to get the next id
        #write that id to the file
        #return the next id

    try:
        with open(filepath, "r") as f:
            last_id = int(f.read().strip())
    except FileNotFoundError:
        print(f"{filepath} file not found; generating new file. IDs will now begin at 1.")
        last_id = 0
    except ValueError: #File exists but is corrupted or empty
        print(f"Cannot generate new task ID; {filepath} does not contain a readable ID.")
        return None
    except OSError as e: #Problem with file i/o such as file permissions denied
        print(f"Cannot generate new task ID; Error opening {filepath} :{e}")
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



#Task Object ----------------------------------------------------------------------------------------------------------------------

class Task:
    priorities = ["High", "Medium", "Low", None]
    statuses = ["Ready", "Active", "Stalled", "Completed"] #"Completed" = Archived

    def __init__(self, 
                 id, 
                 name, 
                 priority = 3,
                 tags = None, 
                 status = statuses[0], 
                 created_at = None):
        self.id = id
        self.name = name
        self.priority = Task.priorities[priority]
        self.tags = tags or []
        self.status = status
        self.created_at = created_at or datetime.now().replace(microsecond = 0).isoformat() #time format = "YYYY-MM-DD*T*HH:MM:SS" ignore asterisks

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "priority": self.priority,
            "tags": self.tags,
            "status": self.status,
            "created_at": self.created_at
        }


#Task Storage Helper Functions ----------------------------------------------------------------------------------------------------


