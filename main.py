from replit import clear
#HINT: You can call clear() to clear the output in the console.
from art import logo
print(logo)

more_visitors = True
visitors = {}
def find_highest_bidder(visitors):
  max_bid = 0
  winner = ''
  for name in visitors:
    bid = visitors[name]
    if bid > max_bid:
      max_bid=bid
      winner = name
  print(f"The winner is {winner} maximum bid is ${max_bid}")
while more_visitors: 
  name = input("What is your name?: ")
  bid = int(input("What is your bid? $ "))
  visitors[name] = bid
  answer = input(("Is there more visitors? 'yes' or 'no'\n")).lower()
  clear()
  if answer == 'no':
    more_visitors = False
    find_highest_bidder(visitors)
  elif answer == 'yes':
    clear()





