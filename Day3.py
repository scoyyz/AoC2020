#! /usr/bin/env python3

map = []

with open("Day3.txt") as file:
  map = file.readlines()  
  file.close()

i = 0
for line in map:
  map[i] = line.strip()
  i += 1

goal = len(map)
width = len(map[0])
slopes = [[1,1,0],[3,1,0],[5,1,0],[7,1,0],[1,2,0]]
result = 1


def count_trees(slope_x, slope_y, trees):
  height = 0 + slope_y
  pos = 0
  while height < goal:
    pos = (pos + slope_x) % width 
    if map[height][pos] == '#':
      trees += 1
    height += slope_y
  return(slope_x,slope_y,trees)

i = 0   
while i < len(slopes):
  slopes[i] = count_trees(slopes[i][0],slopes[i][1], slopes[i][2])
  result *= slopes[i][2]
  i += 1

print(result)