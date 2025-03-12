import datetime

class Task:
  def __init__(self, id, name, description, task_date):
    self.id = id
    self.name = name
    self.description = description
    self.task_date = task_date

  def __str__(self):
    return f"{self.name} {self.description} {self.task_date}"

temp = Task(0, "bego", "test", datetime.datetime.now())
temp1 = Task(1, "bego", "test", datetime.datetime.now())
temp2 = Task(2, "bego", "test", datetime.datetime.now())
Tasks = [temp, temp1, temp2]
flag = True
index = 0

# Name of the app
print("TO_DO App")

# Program main loop 
while flag:
  # Options of the app
  print("What do you want to do?")
  print("1) Modify a task")
  print("2) View your tasks")
  print("3) Exit")
  # Take the option from user
  op1 = input("Please choose a number between 1 and 3 \n")
  #  Option one
  if op1 == "1":
    # Options
    print("1) Add a new task")
    print("2) Update a task")
    print("3) Delete a task")
    
    op = input("Please choose a number between 1 and 3 \n")
    
    # Add new task
    if op == "1":
      name = input("Task name: ")
      description = input("Task description: ")
      joined_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
      t = Task(index ,name ,description, joined_date)
      index =+ 1 
      Tasks.append(t)

    # Update a task
    elif op == "2":
      x = int(input("Please enter the number of the task: "))
      for i in Tasks:
        if i.id == x:
          tempo = i
          break
      if not tempo:
        print("Not Found")
      else:
        print("What do you want to update:")
        print("1) Name")
        print("2) Description")
        z = int(input("Please choose one of the 2 options: "))
        if z == 1:
          new_name = input("Enter the new name: ")
          Tasks[x].name = new_name
        elif z == 2:
          new_desc = input("Enter new description: ")
          Tasks[x].description = new_desc
    elif op == "3":
      pass
  
  elif op1 == "2":
    for i in Tasks:
      print(f"{i.id}){i.name} \n {i.description} \n {i.task_date}")
      print("====================================================")
  elif op1 == "3":
    flag = False


# y = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
# print(y)