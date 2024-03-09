# Add Task: Allow users to add tasks with a title and description.
# List Tasks: Display all the tasks added by the user.
# Mark Task as Done: Allow users to mark tasks as done.
# Delete Task: Allow users to delete tasks.
# Save to File: Save the tasks to a file so they persist between sessions.
# Load from File: Load tasks from the file when the application starts.

class TaskManager:
    def __init__(self) -> None:
        self.task_contents = {}
        self.task_counter = 0
    
    # you could generate a unique task ID automatically within the method. 
    # This way, users of the class won't have to provide a task ID each time they add a task.

    def add_task(self, task:str, task_status:bool):
        self.task_counter += 1
        self.task_contents[self.task_counter] = {"Task desc.": task, "Task status": task_status}
        return self.task_contents
    
    def mark_as_done(self, task_id):
        for i in self.task_contents.keys():
            if i == task_id:
                task_status = True
                self.task_contents[task_id] = {"Task desc.": "Completed", "Task status": task_status}
        return self.task_contents
    
    def remove_task(self, task_id):
        self.task_contents[task_id] = ""
        return self.task_contents

    def __str__(self) -> str:
        HEADER = "\n" + "*-*" + 40 * "-*" + "\n"
        task_str = ""
        task_str += HEADER
        counter = 0
        for i in self.task_contents.items():
            counter += 1
            if counter == 1:
                task_str += f"\n{counter}." + "\t" + str(i) + "\n"
            task_str += f"{counter}." + "\t" + str(i) + "\n"
        task_str += HEADER
        return task_str

my_tasks = TaskManager()

my_tasks.add_task("Go out with the dog",False)
my_tasks.add_task("Clean the kitchen",False)
my_tasks.add_task("Take out the trash",False)
my_tasks.add_task("Clear the yard",False)
my_tasks.add_task("Vaccum the living room",False)
my_tasks.mark_as_done(3)


print(my_tasks)
        