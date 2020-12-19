rules = []
myticket = []
nearbytickets = []

with open("Day16.txt") as file:
  inRules = True
  inNearby = False
  inYour = False
  for line in file:
    if inRules:
      if line == "\n":
        inRules = False
        continue
      rule = line.split(": ")
      values = rule[1].strip().split(" or ")
      for i in range(0,2):
        nums = values[i].split('-')
        values[i] = [int(nums[0]),int(nums[1])]
      rules.append([rule[0],values[0],values[1]])
    elif line == "\n":
      continue
    elif line[0:4] == "your":
      inYour = True
    elif inYour:
      ticket = line[:-1].split(',')
      for num in ticket:
        myticket.append(int(num)) 
      inYour = False
    elif line[0:6] == "nearby":
      inNearby = True
    elif inNearby:
      ticket = line.strip().split(',')
      temp = []
      for num in ticket:
        temp.append(int(num))
      nearbytickets.append(temp)

sum = 0
invalid = []
fields = {}

for ticket in nearbytickets:
  for value in ticket:
    valid = False
    for rule in rules:
      for i in range(1,3):
        if value >= rule[i][0] and value <= rule[i][1]:
          valid = True
    if not valid:
      invalid.append(ticket)

for bad in invalid:
  nearbytickets.remove(bad)

possible = []
length = len(myticket)
for i in range(0,length):
  possible.append(i)
for rule in rules:
  fields[rule[0]] = possible.copy()

for i in range(0,length):
  for ticket in nearbytickets:
    value = ticket[i]
    for rule in rules:
        if not ((value >= rule[1][0] and value <= rule[1][1]) or (value >= rule[2][0] and value <= rule[2][1])):
          fields[rule[0]].remove(i)

test = True
while test:
  for key in fields.keys():
    if len(fields[key]) == 1:
      for k in fields.keys():
        if k != key:
          if fields[key][0] in fields[k]: 
            fields[k].remove(fields[key][0])
  test = False
  for key in fields.keys():
    if len(fields[key]) > 1:
      test = True
      break
      
print(fields)
print(fields.values())
prod = 1

for key in fields.keys():
  if key[:9] == 'departure':
    print(str(key) + ' is index ' + str(fields[key][0]) + ' which for my ticket is ' + str(myticket[fields[key][0]]))
    prod *= myticket[fields[key][0]]
print(prod)
          
      
