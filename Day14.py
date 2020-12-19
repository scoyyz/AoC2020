import re
import math

program = []

with open("Day14.txt") as file:
  for line in file:
    if line[:4] == 'mask':
      program.append(line[7:-1])
    else:
      regex = re.search(r"mem\[(\d*)\] = (\d*)",line)
      program.append([int(regex[1]),int(regex[2])])
  file.close()
  
rules = []
countX = 0

def maskRules(mask):
  rule = []
  count = 0
  for i in range(0,36):
    if mask[i] == 'X':
      rule.append([i,'X'])
      count += 1
    elif mask[i] == '1':
      rule.append([i,'1'])
    else:
      continue
  return rule,count
        
memory = {}
addresses = []

for command in program:
  if isinstance(command,str):
    rules,countX = maskRules(command)
  else:
    addresses.clear()
    binary = bin(command[0])[2:].zfill(36)
    binList = list(binary)
    for rule in rules:
      binList[rule[0]] = rule[1]
    a = 0
    while a < 2**countX:
      addresses.append(0)
      a += 1    
    splits = [[0,len(addresses)]]
    for i in range(0,36):
      if binList[i] == '1':
        for j in range(0,(2**countX)):
          addresses[j] += 2**(35-i)
      if binList[i] == 'X':
        temp = splits.copy()
        splits.clear()
        for split in temp:
          first = int(split[0])
          last = int(split[1])
          mid = int(((split[1]-split[0])/2)+split[0])
          splits.append([first,mid])
          splits.append([mid,last])           
        for j in range(1,len(splits),2):
          start = splits[j][0]
          stop = splits[j][1]
          while start < stop:
            addresses[start] += 2**(35-i)
            start += 1
    for address in addresses:
      memory[address] = command[1]

sum = 0
for key in memory.keys():
  sum += memory[key]

print(sum)
          

      



    
  

    
    
