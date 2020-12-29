import math
import sys

tiles = {}
borders = {}
grid = {}
match = []
directions = {'N':{'N':'F','E':1,'S':0,'W':'RF'},'E':{'N':'RF','E':'F','S':1,'W':0},'S':{'N':0,'E':'RF','S':'F','W':1},'W':{'N':1,'E':0,'S':'RF','W':'F'}}


with open("Day20.txt") as file:
  tileID = ""
  for line in file:
    if line[0] == 'T':
      tileID = line[5:9]
      tiles[tileID]=[]
    elif line == '\n':
      continue
    else:
      tiles[tileID].append(line.strip())
  file.close()

demension = int(math.sqrt(len(tiles)))

def findborders(tile,id):
  length = len(tile[0])
  if tile[0] not in borders.keys():
    borders[tile[0]] = [1]
    borders[tile[0]].append([id,'N'])
  else:
    borders[tile[0]].append([id,'N'])
    borders[tile[0]][0] += 1
  if tile[length-1] not in borders.keys():
    borders[tile[length-1]] = [1]
    borders[tile[length-1]].append([id,'S'])
  else:
    borders[tile[length-1]].append([id,'S'])
    borders[tile[length-1]][0] += 1
  west = ""
  east = ""
  for i in range(0,length):
    west += tile[i][0]
    east += tile[i][length-1]
  if west not in borders.keys():
    borders[west] = [1]
    borders[west].append([id,'W'])
  else:
    borders[west].append([id,'W'])
    borders[west][0] += 1
  if east not in borders.keys():
    borders[east] = [1]
    borders[east].append([id,'E'])
  else:
    borders[east].append([id,'E'])
    borders[east][0] += 1

def removeTile(tile):
  toDelete = []
  for border in borders.keys():
    if tile in borders[border][1]:    
      toDelete.append(border)
    elif len(borders[border]) > 2:
      if tile in borders[border][2]:
        toDelete.append(border)
  for edge in toDelete:
    if tile in borders[edge][1]:
      del borders[edge]
    else:
      borders[edge][0] -= 1
      del borders[edge][2]
    
  
def isMatch(border):
  global match
  if border[0] == 2 and [border[1][1],border[2][1]] in [['N','S'],['S','N'],['E','W'],['W','E']]:
    direction1 = border[1][1]
    direction2 = border[2][1]
    match = [border[1][0],direction1,border[2][0],direction2,directions[direction1][direction2]]
    return True
  else:
    return False

def rotate(tile):
  temp = []
  for line in tile:
    newline = []
    for char in line:
      newline.append(char)
    temp.append(newline)
  tile = list(zip(*temp[::-1]))
  temp = []
  for row in tile:
    string = ""
    for char in row:
      string += char
    temp.append(string)
  return temp

def flip(tile,direction):
  if direction == 'E' or direction == 'W':
    i = 0
    for line in tile:
      tile[i] = line[::-1]
      i += 1
    return tile
  else:
    return tile[::-1]

def addtogrid():
  #print(grid)
  for border in borders:
    #print(borders[border])    
    if isMatch(borders[border]):
      tile1,direction1,tile2,direction2,rotation = match
      if tile1 in grid.keys() and tile2 in grid.keys():
        continue
      if tile1 in grid.keys():
        coord = grid[tile1]
        if direction1 == 'N':
          grid[tile2] = [coord[0],coord[1]+1]
        elif direction1 == 'S':
          grid[tile2] = [coord[0],coord[1]-1]
        elif direction1 == 'E':
          grid[tile2] = [coord[0]+1,coord[1]]
        else:
          grid[tile2] = [coord[0]-1,coord[1]]
      elif tile2 in grid.keys():
        coord = grid[tile2]
        if direction2 == 'N':
          grid[tile1] = [coord[0],coord[1]+1]
        elif direction2 == 'S':
          grid[tile1] = [coord[0],coord[1]-1]
        elif direction2 == 'E':
          grid[tile1] = [coord[0]+1,coord[1]]
        else:
          grid[tile1] = [coord[0]-1,coord[1]]

grid[next(iter(tiles))] = [0,0]

while len(grid) != len(tiles):  
  for tile in tiles:
    if tile not in grid.keys():
      for i in range(0,3):
        tiles[tile] = rotate(tiles[tile])
        borders.clear()
        for found in grid.keys():
          findborders(tiles[found],found)
        findborders(tiles[tile],tile)
        addtogrid()
        if tile in grid.keys():
          break
      if tile not in grid.keys():
        tiles[tile] = flip(tiles[tile],'N')
        borders.clear()
        for found in grid.keys():
          findborders(tiles[found],found)
        findborders(tiles[tile],tile)
        addtogrid()

xcoords = []
ycoords = []   
for value in grid.values():
  xcoords.append(value[0])
  ycoords.append(value[1])

xmin = min(xcoords)
xmax = max(xcoords)
ymin = min(ycoords)
ymax = max(ycoords)
product = 1
corners = [[xmin,ymin],[xmin,ymax],[xmax,ymin],[xmax,ymax]]

### Part 1 Output ###
coords = []
for tile,coord in grid.items():
  coords.append(coord)
  if coord in corners:
    print(tile)
    product *= int(tile)
print(product)


### Part 2 ###

coords = {str(v): k for k, v in grid.items()}

for tile in tiles:
  del tiles[tile][0]
  del tiles[tile][8]
  for i in range(0,len(tiles[tile])):
    tiles[tile][i] = tiles[tile][i][1:-1]

image = []
for y in range(ymax,ymin-1,-1):
  line = ['','','','','','','','']
  for x in range(xmin,xmax+1):
    coord = str([x,y])
    i = 0
    for row in tiles[coords[coord]]:
      line[i] += row 
      i += 1
  for row in line:
    image.append(row)

def isMonster(y,x):
  if image[y-1][x+18] == '#':
    if image[y][x+5] == '#' and image[y][x+6] == '#' and image[y][x+11] == '#' and image[y][x+12] == '#' and image[y][x+17] == '#' and image[y][x+18] == '#' and image[y][x+19] == '#':
      if image[y+1][x+4] == '#' and image[y+1][x+4] == '#' and image[y+1][x+7] == '#' and image[y+1][x+10] == '#' and image[y+1][x+13] == '#' and image[y+1][x+16] == '#':
        return True
  return False

def findMonsters():
  for i in range(1,len(image)-1):
    for j in range(0,len(image[0])-19):
      if image[i][j] == '#':
        if isMonster(i,j):
          monsters.append([i,j])
  


monsters = []
i = 0
while len(monsters) == 0:
  image = rotate(image)
  findMonsters()
  i += 1
  if i == 4:
    image = flip(image,'N')

def markMonsters(y,x):
  image[y-1] = image[y-1][:x+18]+'O'+image[y-1][x+19:]
  image[y] = image[y][:x]+'0'+image[y][x+1:x+5]+'OO'+image[y][x+7:x+11]+'OO'+image[y][x+13:x+17]+'OOO'+image[y][x+20:]
  image[y+1] = image[y+1][:x+1]+'O'+image[y+1][x+2:x+4]+'O'+image[y+1][x+5:x+7]+'O'+image[y+1][x+8:x+10]+'O'+image[y+1][x+11:x+13]+'O'+image[y+1][x+14:x+16]+'O'+image[y+1][x+17:]

print(monsters)

for monster in monsters:
  markMonsters(monster[0],monster[1])

roughseas = 0
for row in image:
  for char in row:
    if char == '#':
      roughseas += 1

print(roughseas)

for row in image:
  print(row)