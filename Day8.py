import re

code = []
with open("Day8.txt") as file:
  code = file.readlines()
  file.close()

executed = []

def reset_executed():
  global executed
  executed.clear()
  i = 0
  while i < len(code):
    executed.append(0)
    i += 1

toChange = []
count = 0

for line in code:
  instr = re.search("([a-z]{3}) ([-\+])(\d+)",code[count])
  if instr[1] == 'nop' or instr[1] == 'jmp':
    toChange.append(count)
  count += 1

reset_executed()
acc = 0
currentInstr = 0
print(toChange)
print(executed)
for change in toChange:
  print(change)
  test = False
  while currentInstr < len(code):
    instr = re.search("([a-z]{3}) ([-\+])(\d+)",code[currentInstr])
    if executed[currentInstr] > 0:
      currentInstr = 0
      acc = 0
      reset_executed()
      break
    executed[currentInstr] += 1
    text = instr[1]
    if currentInstr == change:
      if text == 'nop':
        text = 'jmp'
      else:
        text = 'nop'
    if text == "nop":
      currentInstr +=1
    elif text == "acc":
      currentInstr +=1
      if instr[2] == '-':
        acc -= int(instr[3])
      else:
        acc += int(instr[3])
    else:
     if instr[2] == '-':
       currentInstr -= int(instr[3])
     else:
       currentInstr += int(instr[3])

  
print(change)
print(acc)
