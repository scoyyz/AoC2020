import math

time = 0
busIds = []

with open("Day13.txt") as file:
  line = file.readline()
  time = int(line.strip())
  line = file.readline()
  line.strip()
  for id in line.split(','):
    if id != 'x':
      busIds.append(int(id))
    else:
      busIds.append(id)
  file.close()


rules = {}
for id in busIds:
  if id == 'x':
    continue
  index = busIds.index(id)
  if index == 0:
    rules[id] = [0,0,False]
  else:
    i = 1
    while busIds[index-i] == 'x':
      i += 1
    rules[id] = [i,busIds[index-i],False]

print(rules)

nextDeparture = {}
firstId = busIds[0]
lastId = busIds[-1]
#print(lastId)
timeStamp = (100000000000000 // firstId) * firstId + firstId
#print(timeStamp)
#print(busIds)
increment = math.lcm(busIds[0])
#count = 0
foundIds = [firstId]

 
while True:
  #count += 1
  #print("count is " + str(count))
  #print("timeStamp is " + str(timeStamp))
  distance = 0
  print(nextDeparture)
  for id in busIds:
    #print(nextDeparture)
    #print(rules)
    #print("ID is " + str(id))
    broke = False
    if id in rules.keys():
      distance += rules[id][0]
    if id == 'x':
      continue
    #print(distance)
    depart = ((timeStamp + distance) // id) * id
    #print(depart)
    nextDeparture[id] = depart
    if id == firstId:
      rules[id][2] = True
      continue
    diff = nextDeparture[id]-nextDeparture[rules[id][1]]
    if diff != rules[id][0]:
        timeStamp += increment
        broke = True
        break
    else:
      if id not in foundIds:
        rules[id][2] = True
        foundIds.append(id)
        increment *= id
        # print(distance)
        # print(foundIds)
        # print(increment)
        # print(timeStamp)
  if not broke:
    break
 
print(nextDeparture)
print(nextDeparture[firstId])
      