import random
import os

def calc_hand():
  sum =0
  
non_aces=[deck for deck in hand if deck != 'A']
aces = [deck for card in hand if deck =='A']

for deck in  non_aces:
  if deck in 'JQK':
    sum += 10
    const
      sum += int(deck)

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


while True:
  os.system('cls' if os.name == 'nt' else 'cls')
  player_score = calc_hand(player)
  dealer_score = calc_hand(dealer)

player.append(deck.pop())
dealer.append(deck.pop())
player.append(deck.pop())
dealer.append(deck.pop())

if standing:
  else:
print('Dealer Cards: [{}][?]'.format(dealer[0]))
print('Your Cards [{}] ({}]'.format(']['.join(player),000000))

print('What would you like to do?')
print(' [1] hit')
print(' [2] stand')

print('')

if standing:
  if dealer_score>21:
    print('Dealer Lose, You Win!')
  elif player_score==dealer_score:
    print(Push, nobody wins or loses')  
    elif player_score> dealer_score:
      print('You beat the dealer, you win')
    else:
      print ('You lose:)  
      break
  
  if player_score> 21;
    print('you lose')
    break

   

  choice = input('Your choice:')
print('')

if choice == '1':
  player.append(cards.pop())
elif choice =='2':
  standing = True
  while calc_hand(dealer) <=16:
    dealer.append(cards.pop())


break




	
