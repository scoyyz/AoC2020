player1 = []
player2 = []

with open("Day22.txt") as file:
  current = 0
  for line in file:  
    if line == '\n':
      continue
    elif line[:1] == 'P':
      current = line[7]
    else:
      if current == '1':
        player1.append(int(line.strip()))
      elif current == '2':
        player2.append(int(line.strip()))

def recursivecombat(deck1,deck2):
  # print("Recursive game start")
  # print(deck1)
  # print(deck2)
  states = []
  while True:
    # print(states)
    # print([deck1.copy(),deck2.copy()])
    if [deck1,deck2] in states:
      #print("Recursive game end1")
      return 1 , deck1, deck2
    states.append([deck1.copy(),deck2.copy()])
    # print(states)
    card1 = deck1.pop(0)
    card2 = deck2.pop(0)
    if card1 <= len(deck1) and card2 <= len(deck2):
      win,junk1,junk2 = recursivecombat(deck1[:card1],deck2[:card2])
      if win == 1:
        deck1.append(card1)
        deck1.append(card2)
      else:
        deck2.append(card2)
        deck2.append(card1)
    elif card1 > card2:
      deck1.append(card1)
      deck1.append(card2)
    else:
      deck2.append(card2)
      deck2.append(card1)
    if len(deck1) == 0:
     # print("Recursive game end2")
      return 2 , deck1, deck2
    elif len(deck2) == 0:
      #print("Recursive game end3")
      return 1, deck1, deck2
    # print(deck1)
    # print(deck2)
    # print()
    
# prevstates = []
# theWinner = False
# while True:
  # if [player1,player2] in prevstates:
    # theWinner = True
    # break
  # card1 = player1.pop(0)
  # card2 = player2.pop(0)
  # print(player1)
  # print(player2)
  # print("card1 = " + str(card1) +" and card2 = " + str(card2))
  # if card1 <= len(player1) and card2 <= len(player2):
    # winner = recursivecombat(player1[:card1],player2[:card2])
    # print(winner)
    # print()
    # if winner == 1:
      # player1.append(card1)
      # player1.append(card2)
    # else:
      # player2.append(card2)
      # player2.append(card1)
  # elif card1 > card2:
    # player1.append(card1)
    # player1.append(card2)
  # else:
    # player2.append(card2)
    # player2.append(card1)
  # if len(player1) == 0 or len(player2) == 0:
    # break
  # print(player1)
  # print(player2)
  # print()

def score(deck):
  j = 0
  score = 0
  for i in range(len(deck)-1,-1,-1):
    j += 1
    score += deck[i] * j 
  return score

Winner, player1, player2 = recursivecombat(player1,player2)
    
print(player1)
print(player2)

if len(player1) > 0 or Winner == 1:
  print(score(player1))
else:
  print(score(player2))

