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
    delayPrint("Type 'removed' to see all the cards that have been removed from your hand.")
    delayPrint("Type 'ask' to ask the other player if they have cards of a specific value.")

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
    elif command == "removed":
        printCards("p1Out")
        playerInput()
    elif command == "ask":
        askCard()
    else:
        drawSingleCard("p1")
        delayPrint("'" + command + "' is not a valid command. Please try again. Type 'help' for a list of commands.")
        playerInput()

# Draws one card from the deck for one of the players by counting the number
# of deck cards, choosing a random number from 0 to the amount of deck cards,
# locating that deck card in the whole deck, and assigning it to the
# player's hand
def drawSingleCard(player):
    x = 0
    for i in wholeDeck:
        if i == "deck":
            x+=1
    drawnCard = random.randint(0,x-1)
    counter = 0
    x = 0
    for i in wholeDeck:
        if i == "deck":
            if x == drawnCard:
                wholeDeck[counter] = player
            x+=1
        counter+=1
            

# Draws any number of cards from the deck for one of the players
def drawCards(player, numOfCards):
    for x in range(0, numOfCards):
        drawSingleCard(player)
    if player == "p1":
        printCards("p1")
    makeMatch(player)

# Tells the player what cards they have
def printCards(deck):
    i = 0
    print("\n")
    if deck == "p1":
        delayPrint("The current cards in your hand are:")
    elif deck == "p1Out":
        delayPrint("The current cards removed from your hand are:")
    for card in wholeDeck:
        if wholeDeck[i] == deck:
            delayPrint(str(cardValue[i%13]) + " of " + str(cardSuit[i//13]))
        i+=1

# Checks if one of the players has made a match of four cards
# This entire function is a mess and will eventually be redone
def makeMatch(player):
    cValue = 0
    for card in wholeDeck:
        if card == player:
            ncValue = 0
            for nestedCard in wholeDeck:
                if nestedCard == player:
                    nncValue = 0
                    for nnCard in wholeDeck:
                        if nnCard == player:
                            nnncValue = 0
                            for nnnCard in wholeDeck:
                                if nnnCard == player:
                                    if cValue%13 == ncValue%13 and ncValue%13 == nncValue%13 and nncValue%13 == nnncValue%13 and cValue//13 != ncValue//13 and cValue//13 != nncValue//13 and cValue//13 != nnncValue//13 and ncValue//13 != nncValue//13 and ncValue//13 != nnncValue//13 and nncValue//13 != nnncValue//13:
                                        wholeDeck[cValue] = player + "Out"
                                        wholeDeck[ncValue] = player + "Out"
                                        wholeDeck[nncValue] = player + "Out"
                                        wholeDeck[nnncValue] = player + "Out"
                                        delayPrint(player + " made a match with " + str(cardValue[cValue%13]) + " of " + str(cardSuit[cValue//13]) + ", " + str(cardValue[ncValue%13]) + " of " + str(cardSuit[ncValue//13]) + ", " + str(cardValue[nncValue%13]) + " of " + str(cardSuit[nncValue//13]) + ", and " + str(cardValue[nnncValue%13]) + " of " + str(cardSuit[nnncValue//13]) + ". These cards have been placed out of the game.")
                                nnncValue+=1
                        nncValue+=1
                ncValue+=1
        cValue+=1

def hasValue(player, value):
    counter = 0
    cardsOfValue = 0
    for card in wholeDeck:
        if card == player and cardValue[counter%13] == cardValue[value]:
            cardsOfValue+=1
        counter+=1
    if cardsOfValue == 0:
        return False
    else:
        return True

# This function is a work in progress
# This will allow the player to ask if the other player has a card of any value
def askCard():
    delayPrint("Please type the card value you would like to ask for in its number form.")
    try:
        askedValue = int(input())
        if askedValue < 1 or askedValue > 13:
            delayPrint("That is not a card value. Please try again.")
            askCard()
        elif hasValue("p1", askedValue-1) == False:
            delayPrint("You do not have any cards with this value. Please try again.")
            askCard()
        else:
            askedValue = askedValue - 1
            delayPrint("You have asked Player Two to give you their " + cardValue[askedValue] + "s.")
    except ValueError:
        delayPrint("That is not a valid number. Please try again.")
        askCard()
            
###############################################################################   

# Fills the deck with all 52 cards
for i in range(0,52):
    wholeDeck.append("deck")

drawCards("p1", 5)
drawCards("p2", 5)
delayPrint("It is your turn to ask Player 2 if they have a card you need.")
delayPrint("Type 'help' for a list of commands.")
playerInput()
