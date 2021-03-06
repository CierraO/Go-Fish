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

    if command == "help":
        helpPlayer()
    elif command == "hand":
        printCards("p1")
    elif command == "removed":
        printCards("p1Out")
    elif command == "ask":
        askCard()
        askCardP2()
    else:
        drawSingleCard("p1")
        delayPrint("'" + command + "' is not a valid command. Please try again. Type 'help' for a list of commands.")

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
    if deck == "p1":
        delayPrint("The current cards in your hand are:")
    elif deck == "p1Out":
        delayPrint("The current cards removed from your hand are:")
    for card in wholeDeck:
        if wholeDeck[i] == deck:
            delayPrint(str(cardValue[i%13]) + " of " + str(cardSuit[i//13]))
        i+=1

# Checks if one of the players has made a match of four cards
# This entire function is a mess and might be redone
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
                                        num = 0
                                        for nnnnCard in player:
                                            num+=1
                                        if num == 0:
                                            end = True
                                            delayPrint(player + " has run out of cards. The game is over.")
                                nnncValue+=1
                        nncValue+=1
                ncValue+=1
        cValue+=1

# Checks if a player has any cards of a specific value in their hand
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

# This allows the player to ask if the other player has any cards of a specific value
def askCard():
    delayPrint("Please type the card value you would like to ask for in its number form.")
    try:
        askedValue = int(input())
        if askedValue < 1 or askedValue > 13:
            delayPrint("That is not a card value. Please try again.")
            askCard()
        elif not(hasValue("p1", askedValue-1)):
            delayPrint("You do not have any cards with this value. Please try again.")
            askCard()
        else:
            askedValue = askedValue - 1
            delayPrint("You have asked Player Two to give you their " + cardValue[askedValue] + "s.")
            if not(hasValue("p2", askedValue)):
                delayPrint("Player 2 does not have any cards of this value. You go fish.")
                drawCards("p1", 1)
            else:
                counter = 0
                for card in wholeDeck:
                    if card == "p2" and cardValue[counter%13] == cardValue[askedValue]:
                        wholeDeck[counter] = "p1"
                    counter+=1
                delayPrint("You have been given all of Player 2's cards with this value.")
                makeMatch("p1")
                printCards("p1")
                delayPrint("Since Player 2 had the value you asked for, you get to ask again.")
                askCard()
    except ValueError:
        delayPrint("That is not a valid number. Please try again.")
        askCard()

# This allows Player 2 to ask if the player has any cards of a specific value
def askCardP2():
    x = 0
    for i in wholeDeck:
        if i == "p2":
            x+=1
    card = random.randint(0,x-1)
    counter = 0
    x = 0
    for i in wholeDeck:
        if i == "p2":
            if x == card:
                askedValue = counter%13
                delayPrint("Player 2 is asking you to give them your " + cardValue[askedValue] + "s.")
                if not(hasValue("p1", askedValue)):
                    delayPrint("You do not have any cards of this value. Player 2 goes fish.")
                    drawCards("p2", 1)
                    delayPrint("It is your turn to ask Player 2 if they have a card you need.")
                    delayPrint("Type 'help' for a list of commands.")
                else:
                    nCounter = 0
                    for card in wholeDeck:
                        if card == "p1" and cardValue[nCounter%13] == cardValue[askedValue]:
                            wholeDeck[nCounter] = "p2"
                        nCounter+=1
                    delayPrint("Player 2 has been given all of your cards with this value.")
                    makeMatch("p2")
                    printCards("p1")
                    delayPrint("Since you had the value Player 2 asked for, they get to ask again.")
                    askCardP2()
            x+=1
        counter+=1
            
###############################################################################   

# Fills the deck with all 52 cards
for i in range(0,52):
    wholeDeck.append("deck")

# Gives the players five cards each
drawCards("p1", 5)
drawCards("p2", 5)
delayPrint("It is your turn to ask Player 2 if they have a card you need.")
delayPrint("Type 'help' for a list of commands.")

# Makes the game continue while the game is not over
while not(end):
    playerInput()

# Makes a variable for the number of cards that each player has made a match with
p1Cards = 0
p2Cards = 0

# Counts the number of cards that each player has made a match with
for card in p1Out:
    p1Cards+=1
for card in p2Out:
    p2Cards+=1

# Determines which player has made more matches
if p1Cards > p2Cards:
    delayPrint("You have more matches than Player 2, so you win!")
elif p1Cards < p2Cards:
    delayPrint("Player 2 has more matches than you, so Player 2 wins.")
else:
    delayPrint("You and Player 2 both have the same number of matches, so it's a tie!")

delayPrint("Thanks for playing!")
