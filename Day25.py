
divisor = 20201227
cardkey,doorkey = 8421034,15993936
cardloop = 0
doorloop = 0


def Transform(subject,loopsize):
  result = 1
  for i in range(0,loopsize):
    result *= subject
    result %= divisor
  return result


j = 0
value = 1
while True:
  j += 1
  value *= 7
  value %= divisor
  if value == cardkey:
    cardloop = j
    print("Card loop is " + str(j))
  elif value == doorkey:
    doorloop = j
    print("Door loop is " + str(j))
  if cardloop != 0 and doorloop != 0:
    break

print(cardloop)
print(doorloop)
encrypt = Transform(doorkey,cardloop)

print(encrypt)