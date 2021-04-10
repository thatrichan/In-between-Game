import random
import math

class Player: #OOP for Player class with name and balance
    def __init__ (self, name, balance):
        self.name = name
        self.balance = balance

    def __repr__(self):
        return "Name: {}\nBalance: {}".format(self.name,self.balance)
    
class Cards: #Creating deck of cards
    numbers = {
        1: "Ace",
        2: "Two",
        3: "Three",
        4: "Four",
        5: "Five",
        6: "Six",
        7: "Seven",
        8: "Eight",
        9: "Nine",
        10: "Ten",
        11: "Jack",
        12: "Queen",
        13: "King",
    }

    def __init__(self, suit, number):
        self.suit = suit
        self.number = number

    def __repr__ (self):
        return (self.numbers[self.number]+" of "+self.suit)

    def equals(self,card):
        return self.suit == card.suit and self.number == card.number

class Deck:
    suits = ["Diamond", "Club", "Heart", "Spade"]
    number = [x for x in range (1,14)]

    def __init__ (self):
        self.cards = self.generate_cards()

    def generate_cards(self):
        self.cards = []
        for suit in self.suits:
            for number in self.number:
                self.cards.append(Cards(suit,number))

        random.shuffle(self.cards)
        return self.cards

    def draw_cards(self):
        if self.cards:
            return self.cards.pop()
    
class Pot:
    def __init__(self, balance=0):
        self.balance = balance

    def add_to_pot(self, value):
        self.balance = self.balance + value
        return self.balance

    def withdraw_from_pot(self, value):
        self.balance = self.balance - value
        return self.balance

    def display_balance(self):
        print("Current Pot Value is {} tokens".format(self.balance))


class Game:
    
    def __init__(self):
        self.welcome_message()
        self.story_line()
        self.players = self.set_players()
        self.starting_player_index = 0

    def set_players(self):
        self.players = []
        initial_balance = 100
        for i in range(4):
            name = input("Enter Player {} name:".format(i+1))
            self.players.append(Player(name,initial_balance))
        return self.players

    def add_player_balance(self, value): #add_balance to player
        self.players[i].balance = self.players[i].balance + value
        return self.players[i].balance

    def deduct_player_balance(self, value): #deducts balance off player
        self.players[i].balance = self.players[i].balance - value
        return self.players[i].balance
    
    def story_line(self):
        print("""~~~~~~~~~~~~~~~~~~~~Acey Deucey~~~~~~~~~~~~~~~~~~~~

        In the world of Group 2's Acey Deucey,
        there lives a king, 
        one who is locked up in his own castle,
        who stays alone,
        his king size bed being his only solace,
        the most expensive clothing on his body 
        being his only sense of respite.
        
        His elder told him every day 
        that the world is the source of all evil.
        That it is safer to dwell in the fortress.
        That his only responsibility is to stay alive,
        for the good of their country.
        
        On the night where the moon shone the brightest, 
        He looked out his window only to see 4 
        young and bright children,
        with arms interlinked 
        and small stinky feet dipped into his pond.
        
        The once pristine looking still water,
        rippled with each dip of the children's toe,
        began to rattle the king's heart.
        
        Just like the marred water reflection 
        due to the ripples created unknowingly by the children,
        the king held onto his window still,
        with blood rushing to his tightening hands,
        as his inner peace was broken by the happiness 
        that these young children possess which he dosen't.
        
        In order to escape from the nightmare he is currently in....
            
~~~~~~~~~~~~~~~WILL YOU HELP THE KING FIND HIS INNER PEACE~~~~~~~~~~~~~~~
            
    The 4 children will need to play the game of Acey Deucey 
    in order to obtain 4 keys to the lock on the king's door
    for the king to escape to find his happiness.
    
    In this challenge:
            1. The 4 of you will be given a starting token amount of 100 each
            
            2. To start the pot rolling, the 4 of you have to decide on an equal 
                starting token amount to start the pot rolling
            
            3. Each of you will need to place a bet of your desired amount
            
            4. You will be given 2 cards each containing its value and suits\n
            (ie. Increasing order of Value: Ace, 2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King)\n
            (ie. Siuits are all of equal value: Clubs, Diamonds, Hearts, Spades)
            
            5. You will have to determine how probable it is to choose a card number\n 
            that is in strictly inbetween the 2 cards chosen during your turn in each round 
                
            6. If your card is inbetween both numbers, you will win your intial bet you placed
            
            7. If your card has the same value of the numbers, or lies outside their range,\n
            you will lose you 2 times your initial bet to the pot.
                         
    ~~~~~~~~~~~~~~~ARE YOU READY~~~~~~~~~~~~~~~""")

    def welcome_message(self):
        print("")
        print("         **********************************")
        print("         Welcome to Group 2 In-Between Game")
        print("         **********************************")
        print("")
    
    def details_all_players(self):
        for i in range(4):
            print("Player {}:".format(i+1))
            print(a.players[i])
            print("")

    def bet_amount_valid(self): #
        condition = True
        while (condition):
                bet_value = input("How much do you want to bet (positive integers only)? Type 'quit' to stop: ")
                if (bet_value == "quit"):
                    return bet_value
                try:
                    bet_value = int(bet_value)
                except ValueError:
                    continue
                if(int(bet_value)>a.players[i].balance):
                    print("Bet amount is more than your balance!")
                    continue
                if(int(bet_value)>pot.balance):
                    print("Bet amount is more than the pot balance")
                    continue
                if (bet_value<0):
                    print("Token cannot be negative")
                    continue
                else:
                    condition = False
        return bet_value

    def initial_amount_valid(self):
        condition = True
        while(condition):
            initial_deposit = input("Enter amount to start the pot rolling?")
            try:
                intial_deposit = int(initial_deposit)  
            except ValueError:
                continue
            if (int(initial_deposit)<= 0):
                print("Amount entered cannot be zero or negative")
                continue
            if(initial_deposit.isalpha()):
                print("Amount entered needs to be an integer")
                continue
            if(int(initial_deposit) == a.players[i].balance):
                print("Amount cannot be the same as your balance")
                continue
            if (int(initial_deposit)>a.players[i].balance):
                print("Amount entered is more than what you have")
                continue
            else:
                condition = False
        return int(initial_deposit)

a = Game() #Initialising game
a.welcome_message()#Welcome Message
print("")
a.story_line()
pot = Pot() #Initialising pot
deck = Deck() #Initialising deck of cards

print("")
print("Everyone will start off with 100 token") #Providing initial balance
for i in range(4): #Displaying players details
    print("Player {}:".format(i+1))
    print(a.players[i])
    print("")


print("")
initial_deposit = a.initial_amount_valid() #Starting the pot by putting money 
for i in range(4): #Deduct balance from all players
    a.deduct_player_balance(initial_deposit)
a.details_all_players()

print("") #Displaying pot balance before distributing of cards
pot.add_to_pot(initial_deposit*4)
pot.display_balance()

print("")
while (pot.balance != 0):
    if (pot.balance == 400):
        print("You all have lost the game!")
        break
    else:
        for i in range(len(a.players)): #Iterating 4 players until while condition met
            if(len(deck.cards)<2):
                deck.__init__()
            if (pot.balance == 0):
                print("Congratulation!! Player{} won!!".format(i))
                break
            if(a.players[i].balance ==0):
                continue
            else:
                print("")
                print("Player {}".format(i+1))
                print(a.players[i])
                

                first_card = deck.draw_cards() #Draw First Card
                second_card = deck.draw_cards() #Draw Second Card
                print("{} & {}".format(first_card, second_card)) 
                
                print("")
                bet_amount = a.bet_amount_valid()
                if (bet_amount == "quit"):
                    confirmation = input("Quiting will result in loss of all of your money, are you sure?(y/n)")
                    if(confirmation == "y"):
                        pot.add_to_pot(a.players[i].balance)
                        a.deduct_player_balance(a.players[i].balance)
                        print("")
                        pot.display_balance()
                        #a.players[i].balance = deduct_balance(a.players[i].balance,a.players[i].balance)
                    else:
                        break
                else:
                    bet_amount = int(bet_amount)
                    print("")
                    third_card = deck.draw_cards()
                    print ("Your card is:",third_card)
                    if (first_card.number<third_card.number<second_card.number or second_card.number<third_card.number<first_card.number):
                        print("You've won {} tokens".format(bet_amount))
                        a.add_player_balance(bet_amount)
                        print(a.players[i])
                        pot.withdraw_from_pot(bet_amount)
                        print("")
                        pot.display_balance()
                    elif (first_card.number==third_card.number or second_card.number==third_card.number):
                        if(bet_amount*2>a.players[i].balance):
                            print("Unfortunately, your card is out of range\n{} will be deducted from your balance".format(a.players[i].balance))
                            pot.add_to_pot(a.players[i].balance)
                            a.deduct_player_balance(a.players[i].balance)
                            print(a.players[i])
                            print("")
                            pot.display_balance()
                        else:
                            print("Unfortunately, your card is out of range\n{} will be deducted from your balance".format(bet_amount*2))
                            a.deduct_player_balance(bet_amount*2)
                            print(a.players[i])
                            pot.add_to_pot(bet_amount*2)
                            print("")
                            pot.display_balance()
                    else:
                        print("Unfortunately, your card is out of range\n{} will be deducted from your balance".format(bet_amount))
                        a.deduct_player_balance(bet_amount)
                        pot.add_to_pot(bet_amount)
                        print("")
                        pot.display_balance()
