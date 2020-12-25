
divisor = 20201227
cardkey,doorkey = 8421034,15993936
cardloop = 0
doorloop = 0


def Transform(subject,loopsize):
  value = 1
  for i in range(0,loopsize):
    value *= subject
    value %= divisor
  return value

j = 0
while True:
  j += 1
  print(j)
  result = Transform(7,j)
  if result == cardkey:
    cardloop = j
    print("Card loop is " + str(j))
  elif result == doorkey:
    doorloop = j
    print("Door loop is " + str(j))
  if cardloop != 0 and doorloop != 0:
    break

print(cardloop)
print(doorloop)
encrypt = Transform(doorkey,cardloop)

print(encrypt)