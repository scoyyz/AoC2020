tiles = []

with open("Day24.txt") as file:
  for line in file:
    i = 0
    instruction = []
    while i < len(line):
      if line[i] == '\n':
        break
      elif line[i] == 'e' or line[i] == 'w':
        instruction.append(line[i])
        i += 1
      else:
        instruction.append(line[i:i+2])
        i += 2
    tiles.append(instruction)
 
floor = {}
neighbors = [[1,0],[0,-1],[-1,-1],[-1,0],[0,1],[1,1]]

for tile in tiles:
  coord = [0,0]
  for instruct in tile:
    if instruct == 'e':
      if 'w' in tile:
        tile.remove('e')
        tile.remove('w')
    if instruct == 'se':
      if 'nw' in tile:
        tile.remove('se')
        tile.remove('nw')
    if instruct == 'sw':
      if 'ne' in tile:
        tile.remove('sw')
        tile.remove('ne')
  for instruct in tile:
    if instruct == 'e':
      coord[0] += 1
    elif instruct == 'w':
      coord[0] -= 1
    elif instruct == 'sw':
      coord[0] -= 1
      coord[1] -= 1
    elif instruct == 'se':
      coord[1] -= 1
    elif instruct == 'ne':
      coord[0] += 1
      coord[1] += 1
    elif instruct == 'nw':
      coord[1] += 1
  coordstr = str(coord[0])+','+str(coord[1])
  if coordstr not in floor.keys():
    floor[coordstr] = 'black'
  elif floor[coordstr] == 'white':
    floor[coordstr] = 'black'
  elif floor[coordstr] == 'black':
    floor[coordstr] = 'white'
  for neighbor in neighbors:
    testcoord = []
    for (item1,item2) in zip(coord,neighbor):
      testcoord.append(item1+item2)
    testcoord = str(testcoord[0])+','+str(testcoord[1])
    if testcoord not in floor.keys():
      floor[testcoord] = 'white'
    
black = 0
for tile in floor.keys():
  if floor[tile] == 'black':
    black += 1

print("Part 1: " + str(black))

days = 100

for i in range(0,days):
  floorcopy = floor.copy()
  for tile in floor:
    coords = tile.split(',')
    coord = [int(coords[0]),int(coords[1])]
    count = 0
    for neighbor in neighbors:
      testcoord = []
      for (item1,item2) in zip(coord,neighbor):
        testcoord.append(item1+item2)
      testcoord = str(testcoord[0])+','+str(testcoord[1])
      if testcoord not in floor.keys():
        floorcopy[testcoord] = 'white'
      elif floor[testcoord] == 'black':
        count += 1
    coord = str(coord[0])+','+str(coord[1])
    # print(str(coord)+" is "+floor[coord])
    # print(count)
    if floor[coord] == 'black' and (count == 0 or count > 2):
      floorcopy[coord] = 'white'
    elif floor[coord] == 'white' and count == 2:
      floorcopy[coord] = 'black'
    # print(floorcopy[coord])
    
  floor = floorcopy.copy()
  
     

black = 0
for tile in floor.keys():
  if floor[tile] == 'black':
    black += 1

print("Part 2: "+str(black))