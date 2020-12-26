cups = {}

with open("Day23.txt") as file:
  input = file.readline().strip()
  file.close()
  
length = len(input)
start = int(input[0])
end = int(input[length-1])
for i in range(0,length):
  if i == length - 1:
    cups[int(input[i])] = start
  else:
    cups[int(input[i])] = int(input[i+1])

cups[end] = length + 1
#print(cups)
for i in range(length+1,1000001):
  if i == 1000000:
    cups[i] = start
  else:
    cups[i] = i+1
    
# flag = len(cups) != len(set(cups.values()))
# print(str(flag))

max = 1000000
current = start
for i in range(0,10000000):
  heldstart = cups[current]
  temp = heldstart
  held = []
  for k in range(0,3):
    held.append(temp)
    heldend = temp
    temp = cups[temp]
  target = current - 1 
  if target < 1:
    target = max
  while target in held:
    target -= 1
    if target < 1:
      target = max
  cups[current] = cups[heldend]
  temp = cups[target]
  cups[target] = heldstart
  cups[heldend] = temp
  current = cups[current]



answer = cups[1] * cups[cups[1]]
# print(cups[1])
# print(cups[cups[1]])
print(answer)




