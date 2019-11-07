import random

def calc_hand():
  sum =0
  
non_aces=[deck for deck in hand if deck != 'A']
aces = [deck for card in hand if deck =='A']

for deck in  non_aces:
  if deck in 'JQK':
    sum += 10
    const 
    sum += int('deck')

for deck in aces:
  if sum <= 10:
    sum += 11     
  else:
    sum += 1   

  return sum

def deck ():
  deck 
  [
      2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K, A,
			2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K, A,
			2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K, A,
			2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K, A,
			2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K, A,
]
def cards (): 
    cards = [H,S,D,C]


random.shuffle(deck)

dealer=[]
player=[]
standing = False

if first_hand and player_score==21:
  print ('Blackjack! Awesome')
  break

first_hand = False


while True:
  player_score = calc_hand(player)
  dealer_score = calc_hand(dealer)

player.append(deck.pop())
dealer.append(deck.pop())
player.append(deck.pop())
dealer.append(deck.pop())

Print('Dealer Cards:(dealer[0]')
Print('Player Cards:(Player[0]')

print('What would you like to do?')
print(' [1] hit')
print(' [2] stand')

print('')
choice=input('Your choice: ')
print('')

if standing:
  if dealer_score>21:
    print('Dealer Lose, You Win!')
  
  elif player_score==dealer_score:
    print('Push, wins, loses')  
    
    
    if player_score> dealer_score:
      print('You beat the dealer, you win')
    else:
      print ('You lose')  
      break
  
  if player_score> 21:
    print('you lose')
    break


bank= int(input("How much money do you have:"))
Winnings = 0

done="y"

While game_over == 'y':
  bet=int(input("Bet amount: "))
  if bet > bank:
     print(" Bet amount is more than you have, Try again")
     continue

  else:
      choice=int(input("heads or tails?: "))   
      result=random.radint(0,2)
      if choice == result:
        bank += bet
        winning += bet
        print("You Win")


done= "yes"

  else: 
    bank -= bet
    winnings += bet 
    print("You Lose")    

    print("Bank:",bank) 
    print("You Win")

    done= input( "Play Again? ( y or n): ") 

print("You've made", "winnings", "dollars")
print("You have this much in you bank:", bank)     
   

  choice = input('Your choice:')
   print('')

if choice == '1':
  player.append(cards.pop())
elif choice =='2':
  standing = True
  while calc_hand(dealer) <=16:
    dealer.append(cards.pop())


break




	
