directions = []
with open("Day12.txt") as file:
  for line in file:
    directions.append([line[:1],int(line[1:])])


position = [0,0]
waypoint = [10,1]
  

for instruction in directions:
  if instruction[0] == 'N':
    waypoint[1] += instruction[1]
  elif instruction[0] == 'S':
    waypoint[1] -= instruction[1]
  elif instruction[0] == 'E':
    waypoint[0] += instruction[1]
  elif instruction[0] == 'W':
    waypoint[0] -= instruction[1]
  elif instruction[0] == 'L':
    x,y = waypoint[0],waypoint[1]
    if instruction[1] == 90:
      waypoint[0] = -1*y
      waypoint[1] = x
    elif instruction[1] == 180:
      waypoint[0] = -1*x 
      waypoint[1] = -1*y 
    elif instruction[1] == 270:
      waypoint[0] = y  
      waypoint[1] = -1*x
  elif instruction[0] == 'R':
    x,y = waypoint[0],waypoint[1]
    if instruction[1] == 90:
      waypoint[0] = y
      waypoint[1] = -1*x
    elif instruction[1] == 180:
      waypoint[0] = -1*x 
      waypoint[1] = -1*y 
    elif instruction[1] == 270:
      waypoint[0] = -1*y  
      waypoint[1] = x
  elif instruction[0] == 'F':
     for i in range(0,instruction[1]):
       position[0] += waypoint[0]
       position[1] += waypoint[1]
  else:
    print("Error: Instruction not defined")
    print(instruction[0])
    

print(abs(position[0])+abs(position[1]))