import os
import json
import memory as mem


#ID Related Helper Functions ------------------------------------------------------------------------------------------------------

def get_next_id(filepath = "fern/data/last_id.txt"):
    os.makedirs(os.path.dirname(filepath), exist_ok = True) #checks for the directory (not the file) and creates it if it doesn't exist.
    try:
        with open(filepath, "r") as f:
            last_id = int(f.read().strip())
        return last_id + 1
    
    except (FileNotFoundError, ValueError, OSError):
        print(f"{filepath} file corrupted/empty. Parsing tasks.txt for next open ID:")
        seen_ids = mem.get_used_ids()

        new_id = max(seen_ids, default=0) + 1 #ignores gaps, but always gets u a new, unused number
    
        #try to overwrite the new_id to last_ids
        try:
            with open(filepath, "w") as f:
                f.write(str(new_id))
        except OSError as e:
            print(f"Error creating/writing to {filepath}: {e}")
        
        return new_id



def reset_ids(filepath = "fern/data/last_id.txt"):
    confirm = input(f"Are you sure you want to delete {filepath}? (y/n)\n")
    if confirm.lower() != "y":
        print("Reset cancelled.\n")
        return
    else:
        confirm2 = input(f"Type \"y\" again to confirm the deletion of {filepath}. (y/n)\n")
        if confirm2.lower() != "y":
            print("Reset cancelled.\n")
            return
        else:
            try:
                os.remove(filepath)
                print("File deletion successful: task ID system reset.\n")
            except FileNotFoundError:
                print("File does not exist at specified path.\n")
            except Exception as e:
                print(f"Error occurred during file deletion: {e}\n")


