import random
# upload this to github 
# seems like self only works inside a method of the class 
class cards():
    suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
    ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
    values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 
                'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}

    def __init__(self):
        self.suits = suits 
        self.ranks = ranks
        self.values = values

def values(card):
    return cards.values.get(card) # return the int value of the card in the


def deck(dealer): #use pop instead of remove because it gives the value
    random.shuffle(dealer) # shuffle the card 
    n = random.randint(0,len(dealer)) # make it more robust
    print(f"There are {len(dealer)} cards in the deck")
    return dealer.pop(n), dealer # also returns the newly poped cards
 

#play = input("Press start")

def hitme(dealer,player):
     card = ""
     card,dealer = deck(dealer) # returns the pop and the new card set for the dealers 
     print(f"The dealer drew {card}") # to show what card was drawn. 
     player += values(card) # gets the actuall value of the card 
     return player, dealer # brand new set of delers and cards. 

def stay(dealer,card): # have to get the actually value of the card, use the funtion values
    cards,dealer = deck(dealer) # returns thedealer.pop(random.randint(0,len(dealer))) #dealer gets the ca
    print("The dealter stayed at {}".format(values(cards)))
    card += values(cards)
    return card, dealer # returns the new card they drew and returns the brand new card

# taking in one input the using the logic to adjust it 
class logic(): 
    def __init__(self,dealer,player):
        self.dealer = dealer
        self.player = player 
    ply = ""
    def games_begin(self): # can add another condition to check the cards 
        cards = 0
        while True: # can also be done usning try and catch block 
            ply = input("Do you want to Hit or Stay ")
            if ply == 'H': 
                self.player,self.dealer = hitme(self.dealer,self.player)
                print("You currently have {}".format(self.player))
                if self.player == 21: 
                     print("You win the game !!!! ")
                     break
                elif self.player > 21: 
                      print("You lose the game")
                      break  
            elif ply == 'S':
                cards,self.dealer = stay(self.dealer,cards) # could do a unit test. 
                print(f"The dealer has {cards}")
                if cards == 21: 
                 print("You lose the game")
                 break 
                elif cards > 21: 
                 print("You win the game !!!! ")   
                 break        
            else:
                print("Invalid Input")
                continue 

## the actualy game is played after this point. 
dealer =  list(cards.ranks) * 4  # a game of 52 cards 
player = 0

logic(dealer,player).games_begin()
        

