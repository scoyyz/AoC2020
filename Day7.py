import re

instructions = []

with open("Day7.txt") as file:
  instructions = file.readlines()
  file.close()

bags = {}

counts = {}
  
#part 1 code  

# for rule in instructions:
  # regex1 = re.search('([a-z]* [a-z]*) bag.*contain (.*)',rule)
  # if regex1[2][:2] == 'no':
    # continue
  # else:
    # remainder = regex1[2]
    # test = True
    # while test:
      # regex2 = re.search('(\d*) (\w* \w*).?b?a?g?s?([,\.])(.*)',remainder)
      # if regex2[2] not in bags.keys():
        # bags[regex2[2]] = []
      # bags[regex2[2]].append(regex1[1])
      # if regex2[3] == '.':
        # test = False
      # else:
        # remainder = regex2[4]


    
# test = True
# colors = {'shiny gold':0}
# while test:
  # temp = []
  # for color in colors.keys():
    # if colors[color] == 0:
      # colors[color] = 1
      # if color in bags.keys():
        # for value in bags[color]:
          # temp.append(value)
  # for color in temp:
    # if color not in colors.keys():
      # colors[color] = 0
  # if 0 not in colors.values():
    # test = False

# print(len(colors)-1)

#Part 2 code

for rule in instructions:
  regex1 = re.search('([a-z]* [a-z]*) bag.*contain (.*)',rule)
  if regex1[2][:2] == 'no':
    bags[regex1[1]] = 0
    counts[regex1[1]] = 0
  else:
    remainder = regex1[2]
    bags[regex1[1]] = {"Total":0}
    test = True
    while test:
      regex2 = re.search('(\d*) (\w* \w*).?b?a?g?s?([,\.])(.*)',remainder)
      bags[regex1[1]][regex2[2]] = int(regex2[1])
      if regex2[3] == '.':
        test = False
      else:
        remainder = regex2[4]
      

while 'shiny gold' not in counts.keys():
  for color in bags.keys():
    if color not in counts.keys():
      temp = bags[color].popitem()
      if temp[0] == 'Total':
        counts[color] = temp[1]
      elif temp[0] in counts.keys():
        bags[color]['Total'] += (1 + counts[temp[0]]) * temp[1]
      else:
        bags[color][temp[0]] = temp[1]
     


print(bags)
print(counts)
print(counts['shiny gold'])
  
        