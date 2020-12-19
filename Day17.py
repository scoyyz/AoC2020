input = []

with open("Day17.txt") as file:
  for line in file:
    input.append(line.strip())
    
cubes = {}

def coords(x,y,z,w):
  return str(x) + ',' + str(y) + ',' + str(z) + ',' + str(w)

y=0
z=0
w=0
while y < len(input):
  x = 0
  while x < len(input[y]):
    if input[y][x] == '#':      
      cubes[coords(x,y,z,w)] = '#'
    else:
      cubes[coords(x,y,z,w)] = '.'
    x += 1
  y += 1
  

def addLayer(cubes):
    tempCubes = cubes.copy()
    for cube in cubes:
      current = cube.split(',')
      x,y,z,w = int(current[0]),int(current[1]),int(current[2]),int(current[3])
      for a in range(x-1,x+2):
        for b in range(y-1,y+2):
          for c in range(z-1,z+2):
            for d in range(w-1,w+2):
              coord = coords(a,b,c,d)
              if cube == coord:
                continue
              if coord not in cubes.keys():
                tempCubes[coord] = '.'         
    return tempCubes.copy()
    
iterations = 6

for i in range(0,iterations):
  changes = {}
  cubes = addLayer(cubes)
  tempCubes = cubes.copy()
  for cube in cubes:
    current = cube.split(',')
    x,y,z,w = int(current[0]),int(current[1]),int(current[2]),int(current[3])
    onCount = 0    
    for a in range(x-1,x+2):
      if onCount > 3:
            break
      for b in range(y-1,y+2):
        if onCount > 3:
            break
        for c in range(z-1,z+2):
          if onCount > 3:
            break
          for d in range(w-1,w+2):
            if onCount > 3:
              break
            coord = coords(a,b,c,d)
            if cube == coord:
              continue
            if coord not in tempCubes.keys():
              continue
            if tempCubes[coord] == '#':
              onCount += 1
    if cubes[cube] == '#':
      if not (onCount >= 2 and onCount <= 3):
        changes[cube] = '.'
    elif cubes[cube] == '.':
      if onCount == 3:
        changes[cube] = '#'
    else:
      print("Error: Invalid cube state")
  for change in changes:
    tempCubes[change] = changes[change]
  cubes = tempCubes.copy()

onSum = 0

for cube in cubes.values():
  if cube == '#':
    onSum += 1

print(onSum)
      
          