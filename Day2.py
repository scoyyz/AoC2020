#! /usr/bin/env python3


input = []

with open("Day2.txt") as file:
  for line in file:
    lines = line.split()
    min,max = lines[0].split('-')
    min = int(min)-1
    max = int(max)-1
    char = lines[1].strip(':')
    passwd = lines[2]
    input.append([min,max,char,passwd])
  file.close()

def passwdtest(min,max,char,passwd):
  if passwd[min] == char:
    if passwd[max] == char:
      return False
    return True
  elif passwd[max] == char:
    return True
  else:
    return False
  
    
valid = 0
for pw in input:
  if passwdtest(pw[0],pw[1],pw[2],pw[3]):
    valid += 1
 
print(valid)