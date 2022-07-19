import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

# while continue_play:
#   play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
#   print(logo)
#   if play == 'y':
#     continue_play = True
ulst = []
ulst.append(random.choice(cards))
ulst.append(random.choice(cards))
#print(ulst)

clst = []
clst.append(random.choice(cards))
clst.append(random.choice(cards))
while sum(clst) < 17:
    clst.append(random.choice(cards))

print(clst)
print(sum(clst))
  #   print("Your cards: {}, cureent score: {}".format())
  # elif play == 'n':
  #   continue_play = False
  #   break