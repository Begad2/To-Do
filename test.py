import os 
import json

with open("test.json") as f:
  x = json.load(f)


print(type(x))