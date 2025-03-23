import argparse
import datetime
import json
import os

class Task:
  def __init__(self, id, name, description, joined_date):
    self.id = id
    self.name = name
    self.description = description
    self.joined_date = joined_date

  def to_dict(self):  # Convert to dictionary for JSON serialization
    return {
      "id": self.id,
      "name": self.name,
      "description": self.description,
      "joined_date": self.joined_date
    }

  def __str__(self):
    return f"{self.name}:{self.description}"
  

index = 0
file_name = "./cli_v/tasks.json"

if os.path.exists(file_name) and os.path.getsize(file_name)>0:
  with open(file_name, "r") as f:
    tasks = json.load(f)
    # print(tasks[0])
    # index = tasks[-1].id + 1
else:
  tasks = []



parser = argparse.ArgumentParser(description="A to do list app")
subparsers = parser.add_subparsers(dest="command")

# Add command
add_parser = subparsers.add_parser("add", help="Add a new task")
add_parser.add_argument("name")
add_parser.add_argument("description")

args = parser.parse_args()

if args.command == "add":
  temp = Task(index, args.name, args.description, datetime.datetime.now().strftime("%Y-%m-%d %H:%M"))
  tasks.append(temp.to_dict())
  with open (file_name, "w") as f1:
    json.dump(tasks,f1,indent=4)

# print(Tasks[0])