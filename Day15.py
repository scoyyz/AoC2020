numbers = [0,14,6,20,1,4]
spoken = {0:0,14:1,6:2,20:3,1:4,4:5}
next = 0
i = len(numbers)
while True:
  if next not in spoken.keys():
    spoken[next] = i
    numbers.append(next)
    next = 0
  else:
    distance = i - spoken[next]
    spoken[next] = i
    numbers.append(next)
    next = distance
  i += 1
  if i == (30000000-1):
    print(next)
    break

#print(numbers)
