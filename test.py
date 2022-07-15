dict = {}
auction = True

while auction:
  name = input('what is your name?')
  bid = input('What is your bid?: $')
  dict[name] = int(bid)
  other_bidders = input('Are there any other bidders? yes/no')
  if other_bidders == 'no':
    auction = False