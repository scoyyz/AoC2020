
global rows
rows = []

with open("Day11.txt") as file:
  for row in file:
    rows.append(list(row.strip()))
  file.close()

  
def checkOccupiedP1(x,y):
  occupied = 0
  if y == 0:
    for indexY in range(y,y+2):
      if x == 0:
        for indexX in range(x,x+2):
          if rows[indexY][indexX] == '#':
            occupied += 1
      elif x == length-1:
        for indexX in range(x-1,x+1):
          if rows[indexY][indexX] == '#':
            occupied += 1
      else:
        for indexX in range(x-1,x+2):  
          if rows[indexY][indexX] == '#':
            occupied += 1       
  elif y == len(rows)-1:        
    for indexY in range(y-1,y+1):
      if x == 0:
        for indexX in range(x,x+2):
          if rows[indexY][indexX] == '#':
            occupied += 1
      elif x == length-1:
        for indexX in range(x-1,x+1):
          if rows[indexY][indexX] == '#':
            occupied += 1
      else:
        for indexX in range(x-1,x+2): 
          if rows[indexY][indexX] == '#':
            occupied += 1        
  else:
    for indexY in range(y-1,y+2):
      if x == 0:
        for indexX in range(x,x+2):
          if rows[indexY][indexX] == '#':
            occupied += 1
      elif x == length-1:
        for indexX in range(x-1,x+1):
          if rows[indexY][indexX] == '#':
            occupied += 1
      else: 
        for indexX in range(x-1,x+2): 
          if rows[indexY][indexX] == '#':
            occupied += 1
  return occupied

def checkOccupiedP2(x,y):
  occupied = 0
  #check North
  #print("Check North")
  indexY = y - 1
  while indexY >= 0:
    if rows[indexY][x] == '#':
      occupied += 1
      #print(str(indexY) + ' ' + str(x) + ' ' + str(occupied))
      break
    elif rows[indexY][x] == 'L':
      break
    indexY -= 1
  #check NorthEast
  #print("Check NorthEast")
  indexY = y - 1
  indexX = x + 1
  while indexY >= 0 and indexX < length:
    if rows[indexY][indexX] == '#':
      occupied += 1
      #print(str(indexY) + ' ' + str(indexX) + ' ' + str(occupied))
      break
    elif rows[indexY][indexX] == 'L':
      break
    indexY -= 1
    indexX += 1
  #Check East
  #print("Check East")
  indexX = x + 1
  while indexX < length:
    if rows[y][indexX] == '#':
      occupied += 1
      #print(str(y) + ' ' + str(indexX) + ' ' + str(occupied))
      break
    elif rows[y][indexX] == 'L':
      break
    indexX += 1
  #Check SouthEast
  #print("Check SouthEast")
  indexY = y + 1
  indexX = x + 1
  while indexY < len(rows) and indexX < length:
    if rows[indexY][indexX] == '#':
      occupied += 1
      #print(str(indexY) + ' ' + str(indexX) + ' ' + str(occupied))
      break
    elif rows[indexY][indexX] == 'L':
      break
    indexY += 1
    indexX += 1
  #Check South
  #print("Check South")
  indexY = y + 1
  while indexY < len(rows):
    if rows[indexY][x] == '#':
      occupied += 1
      #print(str(indexY) + ' ' + str(x) + ' ' + str(occupied))
      break
    elif rows[indexY][x] == 'L':
      break
    indexY += 1
  #Check SouthWest
  #print("Check SouthWest")
  indexY = y + 1
  indexX = x - 1
  while indexY < len(rows) and indexX >= 0:
    if rows[indexY][indexX] == '#':
      occupied += 1
      #print(str(indexY) + ' ' + str(indexX) + ' ' + str(occupied))
      break
    elif rows[indexY][indexX] == 'L':
      break
    indexY += 1
    indexX -= 1
  #Check West
  #print("West")
  indexX = x - 1
  while indexX >= 0:
    if rows[y][indexX] == '#':
      occupied += 1
      #print(str(y) + ' ' + str(indexX) + ' ' + str(occupied))
      break
    elif rows[y][indexX] == 'L':
      break
    indexX -= 1
  #Check NorthWest 
  #print("NorthWest")
  indexY = y - 1
  indexX = x - 1
  while indexY >= 0 and indexX >= 0:
    if rows[indexY][indexX] == '#':
      occupied += 1
      #print(str(indexY) + ' ' + str(indexX) + ' ' + str(occupied))
      break
    elif rows[indexY][indexX] == 'L':
      break
    indexY -= 1
    indexX -= 1  

  return occupied

length = len(rows[0])



changed = True
count = 0

while changed:
  count += 1
  toChange = []
  for i in range(0,len(rows)):
    for j in range(0, length):
      if rows[i][j] == 'L':
        if checkOccupiedP2(j,i) == 0:
          toChange.append([i,j])                    
      elif rows[i][j] == '#':
        if checkOccupiedP2(j,i) > 4:
          toChange.append([i,j])
      
  if len(toChange) == 0:
    changed = False     
  
  for coord in toChange:
    y = coord[0]
    x = coord[1]
    if rows[y][x] == 'L':
      rows[y][x] = '#'
    else:
      rows[y][x] = 'L'  
  # for row in rows:
    # print(row)    
  # print()


# for row in rows:
  # print(row)    
# print()


occupied = 0
for row in rows:
  occupied += row.count('#')


print(occupied)