import os
import json
from task import Task
import utils as u

tasks_filepath = "fern/tasks/tasks.txt"
archive_filepath = "fern/tasks/archive.txt"
last_id_filepath = "fern/data/last_id.txt"
memory_verbosity = True

#Task Storage Helper Functions: Saving, Perma-Deletion, Archival
def save_task(task: Task, filepath = tasks_filepath, verbose = memory_verbosity):
    os.makedirs(os.path.dirname(filepath), exist_ok = True) #checks for directory and creates it if it is absent
    try:
        with open(filepath, "a") as f:
            f.write(json.dumps(task.to_dict()) + "\n")
        if verbose:
            print(f"Task: {task.name} (ID: {task.id}) saved to {filepath}.")

    #possible issues: OsError (permissions problem)
    except OSError as e:
        print(f"Error creating/writing task to file: {e}")
        return




#Memory Access/Writing Helper Functions: Last ID Reading/Writing, Duplicate Name/ID Searches, Tag Commonality, etc.

def get_last_id(filepath = last_id_filepath, verbose = memory_verbosity):
    try:
        with open(filepath, "r") as f:
            last_id = int(f.read().strip())
        return last_id
    except (FileNotFoundError, ValueError, OSError): #lastid isn't a number, cant open file, or no file present
        if verbose:    
            print(f"{filepath} file corrupted/empty. Must parse tasks.txt for next open ID.")
        return None


def put_last_id(new_id, filepath = last_id_filepath, verbose = memory_verbosity):
        try:
            with open(filepath, "w") as f:
                f.write(str(new_id))
        except OSError as e:
            if verbose:
                print(f"Error creating/writing to {filepath}: {e}")
        return


def get_used_ids(filepath = tasks_filepath, verbose = memory_verbosity):
    os.makedirs(os.path.dirname(filepath), exist_ok = True)
    seen_ids = set()
    try:
        with open(filepath, "r") as f: #read tasks.txt for seen id's
            for line in f:
                if line.strip():
                    try:
                        task = json.loads(line)
                        seen_ids.add(task.get("id"))
                    except json.JSONDecodeError:
                        continue

    except FileNotFoundError: #if you cant find tasks.txt, its gonna get remade anyway, set seen_ids to empty so the new id is 1
        if verbose:
            print(f"Cannot access tasks.txt. Tasks will now be written to new file.")
    
    return seen_ids



def get_used_names(filepath = tasks_filepath, verbose = memory_verbosity):
    os.makedirs(os.path.dirname(filepath), exist_ok = True)
    seen_names = set()
    try:
        with open(filepath, "r") as f: #read tasks.txt for seen names
            for line in f:
                if not line.strip():
                    continue
                try:
                    task = json.loads(line)
                    seen_names.add(u.normalize_name(task.get("name", "")))
                except json.JSONDecodeError:
                    continue

    except FileNotFoundError: #if you cant find tasks.txt, its gonna get remade anyway
        if verbose:
            print(f"Cannot access tasks.txt. Tasks will now be written to new file.")
    
    return seen_names