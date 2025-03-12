class Begad:
  def __init__(self, name, description):
    self.name = name
    self.description = description

  def __str__(self):
    return f"{self.name}({self.description})"

b1 = Begad("bob", "gamed")
b2 = Begad("bobs", "gameeeed")
# test = ["ana", "bego", "z3lan"]
test = [b1, b2]

for i in test:
  print(i.name)