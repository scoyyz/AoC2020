
input = []

with open("Day18.txt") as file:
  input = file.readlines()
  file.close()
 
def solve(prob):
  data = prob.split(' ')
  while "+" in data:
    i = data.index('+')
    result = int(data[i-1]) + int(data[i+1])
    data[i-1] = result
    del data[i]
    del data[i]
  while "*" in data:
    i = data.index('*')
    del data[i]
  answer = 1
  for num in data:
    answer *= int(num)
  return answer

sum = 0
for problem in input:
  problem = problem.strip()
  for i in range(len(problem)-1,-1,-1):
    if problem[i] == "(":
      for j in range(i,len(problem)):
        if problem[j] == ')':
          problem = problem[:i] + str(solve(problem[i+1:j])) + problem[j+1:]
          break
        if j >= len(problem):
          break
      if i >= len(problem):
          break
  sum+=solve(problem)

print(sum)