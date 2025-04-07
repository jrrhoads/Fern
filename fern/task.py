#Task Object ----------------------------------------------------------------------------------------------------------------------
from datetime import datetime

class Task:
    priorities = ["High", "Medium", "Low", None]
    statuses = ["Ready", "Active", "Stalled", "Completed"] #"Completed" = Archived

    def __init__(self, 
                 id, 
                 name, 
                 priority = 3,
                 tags = None, 
                 status = statuses[0], 
                 created_at = None
                 ):
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
    
    def from_dict(self, dict):
        return Task(
            id = dict["id"],
            name = dict["name"],
            priority = dict.get("priority", None),
            tags = dict.get("tags", []),
            status = dict.get("status", "Ready"),
            created_at = dict.get("created_at") 
        )