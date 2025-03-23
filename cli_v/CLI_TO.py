import argparse
import datetime
import json
import os

class Task:
  def __init__(self, id, name, description, joined_date, status):
    self.id = id
    self.name = name
    self.description = description
    self.joined_date = joined_date
    self.status = status

  def to_dict(self):  # Convert to dictionary for JSON serialization
    return {
      "id": self.id,
      "name": self.name,
      "description": self.description,
      "joined_date": self.joined_date,
      "status": self.status
    }

  def __str__(self):
    return f"{self.name}:{self.description} ==> {self.status}"
  

index = 0
file_name = "./cli_v/tasks.json"

def print_tasks(tasks):
  for task in tasks:
    print(task)

if os.path.exists(file_name) and os.path.getsize(file_name)>0:
  with open(file_name, "r") as f:
    tasks = json.load(f)
    index = tasks[-1]["id"] + 1
else:
  tasks = []



parser = argparse.ArgumentParser(description="A to do list app")
subparsers = parser.add_subparsers(dest="command")

# Add command
add_parser = subparsers.add_parser("add", help="Add a new task")
add_parser.add_argument("name")
add_parser.add_argument("description")

# Update command
update_parser = subparsers.add_parser("update", help="Update a task")
update_parser.add_argument("id")
update_parser.add_argument("description")

# Delete command
delete_parser = subparsers.add_parser("delete", help="Delete a task")
delete_parser.add_argument("id")

# Mark commands
mark_in_prog_parser = subparsers.add_parser("mark_in_progress", help="Mark a task as in progress")
mark_in_prog_parser.add_argument("id")

mark_done_parser = subparsers.add_parser("mark_done", help="Mark a task as done")
mark_done_parser.add_argument("id")

# List command
list_parser = subparsers.add_parser("list", help="List tasks")
# Change status

args = parser.parse_args()

if args.command == "add":
  temp = Task(index, args.name, args.description, datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),"Not done")
  index += 1
  tasks.append(temp.to_dict())
  with open (file_name, "w") as f1:
    json.dump(tasks,f1,indent=4)

elif args.command == "update":
  for i in range(len(tasks)):
    if tasks[i]["id"] == int(args.id):
      tasks[i]["description"] = args.description
  
  for i in range(len(tasks)):
    print(tasks[i])
 
elif args.command == "delete":
  # tasks.pop(int(args.id))
  for i in range(len(tasks)):
    if tasks[i]["id"] == int(args.id):
      tasks.pop(i)
  
elif args.command == "mark_done":
  for i in range(len(tasks)):
    if tasks[i]["id"] == int(args.id):
      tasks[i]["status"] = "Done"
  
elif args.command == "mark_in_progress":
  for i in range(len(tasks)):
    if tasks[i]["id"] == int(args.id):
      tasks[i]["status"] = "InProgress"

elif args.command == "list":
  for i in range(len(tasks)):
    print(tasks[i])
    
print_tasks(tasks)