#Task Object ----------------------------------------------------------------------------------------------------------------------
from datetime import datetime
import utils as u

class Task:
    priorities = ["N/A", "Low", "Medium", "High"]
    statuses = ["Ready", "Active", "Stalled", "Completed"] #"Completed" = Archived

    def __init__(self, 
                 id, 
                 name, 
                 priority = 0,
                 tags = None, 
                 status = 0, 
                 created_at = None
                 ):
        self.id = id
        self.name = name.strip()
        self.priority = priority
        self.tags = tags or []
        self.status = status
        self.created_at = created_at or datetime.now().replace(microsecond = 0).isoformat() #time format = "YYYY-MM-DD*T*HH:MM:SS" ignore asterisks

    @property #stores normalized name as an attribute for prompting i/o: DO NOT STORE IN MEMORY WILL RECALCULATE WHEN ACCESSED
    def name_normalized(self):
        return u.normalize_name(self.name)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "priority": self.priority,
            "tags": self.tags,
            "status": self.status,
            "created_at": self.created_at
        }
    
    def from_dict(self, dict):
        return Task(
            id = dict["id"],
            name = dict["name"],
            priority = dict.get("priority", Task.priorities[0]),
            tags = dict.get("tags", []),
            status = dict.get("status", Task.statuses[0]),
            created_at = dict.get("created_at") 
        )