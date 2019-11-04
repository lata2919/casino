from random import shuffle
#A function for creating a deck
#Suites: H, S, D, C - Ranks: A, 2-9, T, J, Q, K,
#return a shuffled deck with 52 cards
def deck():
    deck = []
    for Suit in ['H','S', 'D','C'] :
        for card in ['A','2','3','4','5','6','7','8','9','J','Q','K','T']:
            deck.append "suit + card"

    shuffle(deck)

    return deck

# A function for counting the points
# takes in the players card and return the total points
def  pointcount (playercards):
     Playercount= 0

     for i in playercards:
         if(i)[1] == 'J' or i[1] == 'Q' or i[1] == 'K' or i[1] == 'T':
             playercount += 10
             if (i[1] != 'A'):
                mycount += int(i[1]) 
             else:
                 acecount += 1
                 if (acecount ==1 and playercount >= 10):
                     mycount += 11
                     elseif(aceCount != 0)
                     playercount += 1 
                     return playercount

#A function for creating the player's and dealer's hand
#randomly gives each two cards from deck
#return a list with both hands
def createPlayingHands(mydeck):
    dealerHand =[]
    playerhand =[]
    dealerHand.append(mydeck.pop())
    dealerHand.append(myDeck.pop())
    playerHand.append(myDeck.pop())
    playerHand.append(myDeck.pop())

    while(pointCount (dealerHand)<-16):
        dealearHand.append(myDeck.pop())

        Return [dealerHand, playerHand]
#here we create the game
#game loop

game=""
myDeck = deck()
hands = createPlayingHands(myDeck)
dealer= hands[0]
player= hands[1]

while(game !="exit"):
    dealercount = pointCount(dealer)
    playerCount = pointCount(player)

    print ("Dealer has:")
    print (dealer[0])

    print ("Player1, you have:")
    print (player)

    if(playercount ==21):
        print ("Blackjack! Player win!!")
        break
    if (playerCount > 21):
        print ("Player BUSTS! With " + str(playerCount) + "points")
        break
    if(dealerCount > 21):
        print ("Dealer BUSTS! With " + str(dealerCount) + "points")
        break
    
    game = raw_input("What would you like to do? H: Hit me, S: Stand?")

    if(game== 'H'):
        player.append(myDeck.pop())
   
    if ("playercount > dealercount"):   
     print ("Player wins with" + str(playerCount) +"points")
     print ("Dealer has:"+ str(dealer) + "or" + str(dealerCount)+ "points")
    break
else:
    print ("Dealer wins!")
    print ("Dealer has:" + str(dealer) + "or " + str(dealer) + "points")
    break

#player cash out anytime
#player set dollar amount
#player wallet able to add money
#winnings added to dollar amount