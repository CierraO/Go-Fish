## @file:   Go Fish.py
#  @author: Cierra
#  @date:   5/17/18
#

import random
import sys
import time

end = False
# List of the positions of all cards
# The values are grouped by suit, in the order they are listed in cardSuit
wholeDeck = []
cardValue = ["Ace", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King"]
cardSuit = ["Hearts", "Spades", "Diamonds", "Clubs"]

# This makes each letter show up one at a time
def delayPrint(text):
    for c in text:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.035)
    print("\n")

# This tells the player all of the commands they can use
def helpPlayer():
    delayPrint("Type 'hand' to see all the cards in your hand.")
    delayPrint("Type 'out' to see all the cards in your 'out' pile.")
    delayPrint("Type 'ask' to ask the other player if they have a specific card.")

# This allows the player to type and use commands
def playerInput():
    command = input()
    command = command.lower()

    if end:
        delayPrint("The game is over.")
    elif command == "help":
        helpPlayer()
        playerInput()
    elif command == "hand":
        printCards("p1")
        playerInput()
    elif command == "out":
        printCards("p1Out")
        playerInput()
    elif command == "ask":
        delayPrint("This does not work yet.")
        askCard()
    else:
        drawSingleCard("p1")
        delayPrint("'" + command + "' is not a valid command. Please try again. Type 'help' for a list of commands.")
        playerInput()
## @COMMENT:
#  5) In the comment section for this function,
#  explain how you are drawing a single card
#  6) Re-evaluate how you are drawing a single card.
#  What are the differences in how a card is drawn
#  (compare with your code):
#    for i in wholeDeck:
#        if i == "deck":
#            if x == drawnCard:
#                wholeDeck[counter] = player
#            x+=1
#        counter+=1
#

# Draws one card from the deck for one of the players
def drawSingleCard(player):
    x = 0
    for i in wholeDeck:
        if i == "deck":
            x+=1
    drawnCard = random.randint(0,x-1)
    counter = 0
    x = 0
    # 6) Compare with code above
    for i in wholeDeck:
        if i == "deck" and counter == drawnCard:
            x+=1
            wholeDeck[counter] = player
        counter+=1
            

# Draws any number of cards from the deck for one of the players
def drawCards(player, numOfCards):
    for x in range(0, numOfCards):
        drawSingleCard(player)
    if player == "p1":
        printCards("p1")
    makeMatch(player)

## @COMMENT:
#  7) Is the print("\n") at the end of this function necessary?
#  The delayPrint() function already includes this at the end.
#

# Tells the player what cards they have
def printCards(deck):
    i = 0
    print("\n")
    delayPrint("The current cards in your pile are:")
    for card in wholeDeck:
        if wholeDeck[i] == deck:
            delayPrint(str(cardValue[i%13]) + " of " + str(cardSuit[i//13]))
        i+=1
    print("\n")

## @COMMENT:
#  8) The requirement for a player to score points in this game is to have 4
#  cards of the same 'value' in their hand. Remove cards from a players hand
#  to the out of game pile only when they have 4 of the same 'value'.
#  9) You should not be checking for a match with cards outside of the game.
# 

# Checks if one of the players has made a match
def makeMatch(player):
    # Checks if a player has a match within their hand
    cValue = 0
    for card in wholeDeck:
        if card == player:
            ncValue = 0
            for nestedCard in wholeDeck:
                if nestedCard == player:
                    if cValue%13 == ncValue%13 and cValue//13 != ncValue//13:
                        wholeDeck[cValue] = player + "Out"
                        wholeDeck[ncValue] = player + "Out"
                        delayPrint(player + " made a match with " + str(cardValue[cValue%13]) + " of " + str(cardSuit[cValue//130]) + " and " + str(cardValue[ncValue%13]) + " of " + str(cardSuit[ncValue//13]) + ". These cards have been placed out of the game.")
                ncValue+=1
        cValue+=1
    # Checks if a player has a match between a card in their hand and cards out of the game
    cValue = 0
    for card in wholeDeck:
        if card == player:
            ncValue = 0
            for nestedCard in wholeDeck:
                if nestedCard == player + "Out":
                    if cValue%13 == ncValue%13 and cValue//13 != ncValue//13:
                        wholeDeck[cValue] = player + "Out"
                        delayPrint(player + " made a match with " + str(cardValue[cValue%13]) + " of " + str(cardSuit[cValue//130]) + " and cards in their out-of-the-game pile. This card has been placed out of the game.")
                ncValue+=1
        cValue+=1

# This function is a work in progress
# This will allow the player to ask if the other player has a card of any value
def askCard():
    print("")
            
###############################################################################   

# Fills the deck with all 52 cards
for i in range(0,52):
    wholeDeck.append("deck")

drawCards("p1", 5)
drawCards("p2", 5)
delayPrint("Type 'help' for a list of commands.")
playerInput()
