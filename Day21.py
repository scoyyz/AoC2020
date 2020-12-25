import re

input = []
allergens = {}
ingredients = {}
translated = set()

with open("Day21.txt") as file:
  for line in file:
    regex = re.search(r"([\w ]*) \(contains (.*)\)",line)
    input.append([regex[1].split(' '),regex[2].split(', ')])
  file.close()

for line in input:
  for food in line[0]:
    if food not in ingredients:
      ingredients[food] = 1
    else:
      ingredients[food] += 1
  for allergen in line[1]:
    if allergen not in allergens.keys():
      allergens[allergen] = []
    allergens[allergen].append(line[0])
    
for allergen in allergens:
  result = set(allergens[allergen][0])
  for ingredient in allergens[allergen]:
    result.intersection_update(ingredient)
  allergens[allergen] = result

while True:
  test = True
  for allergen in allergens:
    if len(allergens[allergen]) == 1:
      word = allergens[allergen].pop()
      allergens[allergen].add(word)
      translated.add(word)
      for key in allergens.keys():
        if key != allergen:
          if word in allergens[key]:
            allergens[key].remove(word)
    else:            
      test = False
  if test:
    break

 

  
nonallergens = set(ingredients.keys()).difference(translated)

count = 0

for item in nonallergens:
  count += ingredients[item]

print(count)
part2 = ""

for key in sorted(allergens.keys()):
  part2 += allergens[key].pop() + ','
  
print(part2[:-1])