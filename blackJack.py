###################################
#####  Black Jack In Python   #####
###################################

#
# Rules of Simple Blackjack:






# * No matter what the player chooses, the dealer shows their second card and must hit again if their hand is below 17
# * Once both the dealer and the player have drawn/not drawn, the values are added up and a winner is determined
# * The hands are resolved in this order:
#     1) Player Blackjack
#     2) Dealer Blackjack
#     3) Player bust
#     4) Dealer bust
#     5) Raw total
#
# Use classes! Classes make this easier than it sounds. When I wrote this, I made a class for the deck and a class for an individual
#                                                                                       ^^^ I like this




class deck:
                     #cards
    deck = [2,3,4,5,6,7,8,9,10,11,12,13,14]
    def deal(self):
        self.deck = self.deck

class user:
    userHand = []
    def usersHand(self):
        self.userHand = self.userHand
    
    
# card. Here's a rough outline of how I went about writing this:
#
# * Create a card class that contains 2 variables, suit and value
# * Create a deck class that has functions to create/initialize the deck, shuffle the deck, and draw a card
# * In the main program, when the program first starts up, call the function to initialize the deck and shuffle the deck
# * Then call the draw card function as needed and keep track of the cards drawn
#
# Tips/Tricks
# * A List in python can easily be used as a stack since there's a built-in pop() function. Pop() returns the last item in the List
# and removes it from the List. I highly recommend using a List to store the Card objects. To draw a card, all you have to do is
# call pop() and that's it!
# * I'll just give you guys the shuffle algorithm because I wasn't happy with any of the methods I came up with and decided to
# look up common ones. Here's an implementation of the Fisher-Yates shuffle algorithm straight from my program:
#
#
#     ## Shuffles the deck using an implementation of the Fisher-Yates shuffle algorithm.
#     #
#     # @param self The object pointer for the current instance.
#     def shuffle_deck(self):
#         maximum = 51
#         for index in range(51, 0, -1):
#             card_to_swap = random.randint(0, maximum)
#             temp_card = self.deck[card_to_swap]
#             self.deck[card_to_swap] = self.deck[index]
#             self.deck[index] = temp_card
#             maximum = maximum - 1
import os
import random

                # * Dealer draws 2 cards, but only one is shown
                #
                 # * Player draws 2 cards, both are shown
                 # * Player chooses whether to stay or hit

                 # AI and User
dealer = 'computer'
player = 'user'
                # AI functions

                # def drawingCards (){
                #
                # }

dealerHand = []
playerHand = []




## * Pip cards are worth their face value
pipcard =  cardsValue


# * Face cards are all worth 10
facecards =

# * Aces are always high, worth 11
ace = 11

# * Object is to get a better hand than the dealer, without the value of your hand going above 21


