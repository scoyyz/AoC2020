groups = []

#Read input
with open("Day6.txt") as file:
  group = []
  for line in file:
    #check if line is an empty line indicating the end of a group
    if line == "\n":
      groups.append(group)
      group = []
    #add line to the list for this group, removing the new line
    else:
      group.append(line.strip())
  file.close
  
sum = 0

for grp in groups: #look at each group individually
  answers = {} 
  for form in grp: #look at each form in a group
    for char in form: #look at each character/answer on that form
      #check to see if key already exists in dictionary and either initialize it or increment it accordingly
      if char in answers.keys():
        answers[char] += 1
      else:
        answers[char] = 1
  #look at each key in the dictionary. If the value matches the number of forms in this group, increment the total sum
  for key in answers.keys():
    if answers[key] == len(grp):  
      sum += 1

print(sum)