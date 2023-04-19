############### Blackjack Project #####################

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.
################################################################
import random
import replit
from art import logo 

def deal_card():
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  return random.choice(cards)

def calculate_score(card_list):
  if sum(card_list) == 21 and len(card_list) == 2:
    return 0
  elif sum(card_list) > 21 and 11 in card_list:
    card_list.remove(11)
    card_list.append(1)
    return sum(card_list)
  return sum(card_list)

#Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.
def compare(user_score, dealer_score):
  if user_score == dealer_score:
    print(f"Draw! 🙃")
  elif dealer_score == 0:
    print(f"You Lose! Dealer has Blackjack 😵")
  elif user_score == 0:
    print(f"You got Blackjack! You Win! 😎")
  elif user_score > 21:
    print(f"You overdrew! You Lose! 🤯")
  elif dealer_score > 21:
    print(f"Dealer overdrew! You Win! 🤭")
  elif dealer_score > user_score:
    print(f"You Lose! Dealer score is higher! 🥺")
  else:
    print(f"You Win! Your score is higher! 😁")
    
    

def play_game():
  user_cards = []
  dealer_cards = []

  print(logo)
  
  for _ in range(2):
    user_cards.append(deal_card())
    dealer_cards.append(deal_card())

  game_end = False
  while not game_end:
    user_score = calculate_score(user_cards)
    dealer_score = calculate_score(dealer_cards)
    print(f"Your cards: {user_cards}, current score {user_score}")
    print(f"Dealer's first card: [{dealer_cards[0]}]")
    #Game End Condition if blackjack by dealer
    if user_score == 0 or dealer_score == 0 or user_score > 21:
      game_end = True
    else:
      draw_choice = input("Do you want to draw another card? Type 'y' for yes or 'n' for no: ").lower()
      if draw_choice == 'y':
        user_cards.append(deal_card())
      else:
        game_end = True
  
  while dealer_score < 17 and dealer_score != 0 and user_score < 22:
    dealer_cards.append(deal_card())
    dealer_score = calculate_score(dealer_cards)
  print(f"Your final hand: {user_cards}, final score {user_score}")
  print(f"Dealer's final hand: {dealer_cards}, final score {dealer_score}")
  compare(calculate_score(user_cards), calculate_score(dealer_cards))
  
while input("Do you want to play a game of Blackjack? Type 'y' for yes or 'n' for no: ") == "y":
  replit.clear()
  play_game()



