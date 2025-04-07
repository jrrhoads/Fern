
import task_manager as tm
from task import Task



#task creation debug/testing
test_id = tm.get_next_id()
test_task = Task(test_id, "Fold laundry", 2)

print(f"{test_task.id}, {test_task.name}, {test_task.priority}, {test_task.tags}, {test_task.status}, {test_task.created_at}")


test_id2 = tm.get_next_id()
test_task2 = Task(test_id2, "Wash Dishes", 0)

print(f"{test_task2.id}, {test_task2.name}, {test_task2.priority}, {test_task2.tags}, {test_task2.status}, {test_task2.created_at}")


#reset_ids debug/testing
tm.reset_ids()

tm.reset_ids()

tm.reset_ids()
