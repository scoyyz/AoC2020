
seats = []
highest = 0

with open("Day5.txt") as file:
  seats = file.readlines()
  file.close()
  
for seat in seats:
  row = 0
  column = 0
  if seat[0] == 'B':
    row += 64
  if seat[1] == 'B':
    row += 32
  if seat[2] == 'B':
    row += 16
  if seat[3] == 'B':
    row += 8
  if seat[4] == 'B':
    row += 4
  if seat[5] == 'B':
    row += 2
  if seat[6] == 'B':
    row += 1  
  if seat[7] == 'R':
    column += 4
  if seat[8] == 'R':
    column += 2
  if seat[9] == 'R':
    column += 1
  test = row * 8 + column
  if test > highest:
    highest = test

print(highest)