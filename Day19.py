import re

rules = {}
messages = []
solvedRules = []

with open("Day19.txt") as file:
  for line in file:
    if line[0].isnumeric():
      regex = re.search(r"(\d+): (.+)",line)
      rules[regex[1]] = regex[2]
    elif line[0].isalpha():
      messages.append(line.strip())
  file.close()


gate = True
while gate:
  gate = False
  #print(solvedRules)
  for key in rules.keys():
    if rules[key][0] == '"':
      rules[key] = rules[key][1]
      solvedRules.append(key)
      gate = True
    elif rules[key][0].isalpha() or rules[key][0] == '(' or key in ['0','11']:
      continue
    elif key == '8':
      if '42' in solvedRules:
        rules[key] = "(?:"+rules['42']+")+"
        solvedRules.append(key)
    if '|' in rules[key] and key != '8':
      halves = rules[key].split(' | ')
      conditions = (halves[0]+' '+halves[1]).split(' ')
      test = True
      #print(conditions)
      for condition in conditions:
        if condition not in solvedRules:
          test = False
      if test:
        rule = "(?:"
        for i in range(0,int(len(conditions)/2)):
          rule += rules[conditions[i]]
        rule += "|"
        for i in range(int(len(conditions)/2),len(conditions)):
          rule += rules[conditions[i]]
        rule += ")"
        #print(rule)
        rules[key] = rule
        solvedRules.append(key)
        gate = True
    else:
      conditions = rules[key].split(" ")
      test = True
      for condition in conditions:
        if condition not in solvedRules:
          test = False
      if test:            
        rule = "(?:"
        for condition in conditions:
          rule += rules[condition]
        rule += ")"
        rules[key] = rule
        solvedRules.append(key)
      gate = True

valid = 0

for message in messages:
  for n in range(1,100):
    N = "{"+str(n)+"}"
    pattern = rules['8']+rules['42']+N+rules['31']+N
    match = re.fullmatch(pattern,message)
    if match:
      valid += 1
      break

print(valid)
