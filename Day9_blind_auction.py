from replit import clear
#HINT: You can call clear() to clear the output in the console.
from Day9_art import logo
print(logo)

dict = {}
auction = True

## Indent all the selected codeL
## ctrl + ]
while auction:
  name = input('what is your name?')
  bid = int(input('What is your bid?: $'))
  dict[name] = bid
  other_bidders = input('Are there any other bidders? yes/no \n')
  if other_bidders == 'no':
    auction = False
  elif other_bidders == 'yes':
    clear()

maxbid = 0
winner = ''

ks = dict.keys()
for k in ks:
  if dict[k] > maxbid:
    winner = k
    maxbid = dict[k]
print('The winner is {} with a bid of ${}'.format(winner, maxbid))