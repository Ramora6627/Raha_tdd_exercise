VALID_CARDS = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King', 'Ace']

def blackjack_score(hand):
  valid = 0
  flag = 0
  total = 0
  if(set(hand).issubset(set(VALID_CARDS))):
    flag = 1
  if 2 <= len(hand) <= 5:
    valid = 1
    
  if flag and valid:
    for i in hand:
      if i in ["Jack", "Queen", "King"]:
        value = 10
        total += value 
      elif i == "Ace":
        if total + 11 > 21:
          value == 1
          total += 1
          print (total)
        elif total + 11 <= 21:
          value = 11
          total += value
          print (total)
      elif 2 <= i <= 10:
        value = i
        total += value
      
  else:
    total = "invalid"
  if total != "invalid" and total > 21:
    total= "bust"
  return total

  # pass