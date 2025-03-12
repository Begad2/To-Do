import datetime

class Task:
  def __init__(self, name, description, task_date):
    self.name = name
    self.description = description
    self.task_date = task_date

Tasks = []

print("TO_DO App")
flag = True
while flag:
  print("What do you want to do?")
  print("1)Modify a new task")
  print("1) Modify a new task")
  print("2) View your tasks")
  print("3) Exit")
  op1 = input("Please choose a number between 1 and 3 \n")
  if op1 == "3":
    flag = False
  elif op1 == "1":
    print("1) Add a new task")
    print("2) Update a task")
    print("3) Delete a task")
    op = input("Please choose a number between 1 and 3 \n")



  

# y = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
# print(y)