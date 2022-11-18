#this is a function in replit that clears the screen after each entry
from replit import clear
#import the logo ascii art from the art module
from art import logo
#print the logo
print(logo)

#create a variable to use for the continuone running of the code in a while loop
more_bidders = False
#a variable storing an empty dictionary
all_bid = {}

#this function helps to dtermine the highest bidder by passing the all_bid dictionary as an argument
def find_highest_bidder(bidding_record):
  highest_bid = 0
  winner = ""
  for bidder in bidding_record:
    bid_amount = bidding_record[bidder]
    if bid_amount > highest_bid: 
      highest_bid = bid_amount
      winner = bidder
  print(f"The winner is {winner} with a bid of ${highest_bid}")


#the loop will continue to run until the more_bidders variable created earlier becomes true which can only be if the input says no more bidders.   
while more_bidders != True:
    name = input('what is your name?')
    bid = int(input('what is your bid?'))
    all_bid[name] = bid
    asking = input('Do you have more bidders, type "yes" or "no"')
    if asking == 'yes':
        more_bidders = False
        clear()
    else:
        more_bidders = True
        find_highest_bidder(all_bid)
