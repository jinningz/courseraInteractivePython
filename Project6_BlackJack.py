# Mini-project #6 - Blackjack

import simplegui
import random

# load card sprite - 936x384 - source: jfitz.com
CARD_SIZE = (72, 96)
CARD_CENTER = (36, 48)
card_images = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/cards_jfitz.png")

CARD_BACK_SIZE = (72, 96)
CARD_BACK_CENTER = (36, 48)
card_back = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png")    

# initialize global variables
in_play = False
outcome = ""
score = 0

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}



# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
    
    # A drawing function to draw the back of a card    
    def draw1(self, canvas, pos):
        card_loc = (CARD_CENTER[0], CARD_CENTER[1])
        canvas.draw_image(card_back, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
            
    
# define hand class
class Hand:
    def __init__(self):
        # create Hand object (a list of card objects)
        self.cards_in_hand = []

    def __str__(self):
        # return a string representation of a hand
        self.card_in_hand_string = ""
        for i in range(len(self.cards_in_hand)):
            self.card_in_hand_string += " " + self.cards_in_hand[i].suit + self.cards_in_hand[i].rank 
        return "Hands contains" + self.card_in_hand_string

    def add_card(self, card):
        # add a card object to a hand
        self.cards_in_hand.append(card) 

    def get_value(self):
        # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
        # compute the value of the hand, see Blackjack video
        
        hand_str = ""
        hand_value = 0
        
        for i in range(len(self.cards_in_hand)):
            # Concatenate all cards rank for evaluation if Ace
            hand_str += self.cards_in_hand[i].get_rank()
            # Sum up card values
            hand_value += VALUES[self.cards_in_hand[i].get_rank()]

        # If Ace is not one of the cards in hand
        if hand_str.find('A') == -1:
            return hand_value
        else: # If Ace is one of the cards in hand
            if hand_value + 10 <= 21:
                return hand_value + 10
            else:
                return hand_value

    def draw(self, canvas, pos):
        # draw a hand on the canvas
        for i in min(range(len(self.cards_in_hand)), range(5)):
            self.cards_in_hand[i].draw(canvas, [pos[0] + (i * 75), pos[1]])
 
        
# define deck class 
class Deck:
    def __init__(self):
        
        # create a Deck object
        self.cards_in_deck = []
        
        # a deck of 52 cards
        for i in range(len(SUITS)):
            for j in range(len(RANKS)):
                self.cards_in_deck.append(Card(SUITS[i], RANKS[j]))
        
    def shuffle(self):
        # shuffle the deck 
        random.shuffle(self.cards_in_deck)

    def deal_card(self):
        # deal a card object from the deck
        deal = self.cards_in_deck[-1]
        # remove the card from deck
        self.cards_in_deck.pop(-1)
        return deal
    
    def __str__(self):
        # return a string representing the deck
        self.cards_in_deck_string = ""
        for i in range(len(self.cards_in_deck)):
            self.cards_in_deck_string += " " + self.cards_in_deck[i].suit + self.cards_in_deck[i].rank
        return "Deck contains" + self.cards_in_deck_string


# define event handlers for buttons
def deal():
    global outcome, score, in_play, deck, dealer, player

    # Initialize global variables
    deck = Deck()
    deck.shuffle()
    
    dealer = Hand()
    player = Hand()
    
    outcome = ""
    
    for i in range(2):
        dealer.add_card(deck.deal_card())
        player.add_card(deck.deal_card())
    
    # If player exits during the middle of game
    if in_play:
        score -= 1
        outcome = "Player gives up"
    
    in_play = True
    

def hit():
    # if the hand is in play, hit the player
    global outcome, score, in_play, player
    
    if in_play:
        player.add_card(deck.deal_card())
        if player.get_value() > 21:
            outcome = "You have busted."
            in_play = False
            score -= 1

            
def stand():
    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more
    global outcome, score, in_play, player
    
    if in_play:
        while dealer.get_value() < 17:
            dealer.add_card(deck.deal_card()) 

        if dealer.get_value() > 21:
            outcome = "Dealer busted. You win."
            score += 1
        else:
            if dealer.get_value() < player.get_value():
                outcome = "You win."
                score += 1
            else:
                outcome = "You lose."
                score -= 1
    else:
        outcome = "You hand is already busted."
        
    in_play = False


# draw handler    
def draw(canvas):
    
    # Draw titles
    canvas.draw_text("Blackjack", [75, 100], 50, "Blue")
    canvas.draw_text("Score " + str(score), [450, 100], 30, "Black")
    
    # Draw dealer info
    canvas.draw_text("Dealer", [50, 175], 30, "Black")
    canvas.draw_text(outcome, [200, 175], 30, "Black")
    
    dealer.draw(canvas, [50, 200])
    # Hide dealer's first card
    if in_play:
        dealer.cards_in_hand[1].draw1(canvas, [50, 200])
    
    # Draw player info
    canvas.draw_text("Player", [50, 375], 35, "Black")
    
    if in_play:
        canvas.draw_text("Hit or stand?", [200, 375], 30, "Black")
    else:
        canvas.draw_text("New deal?", [200, 375], 30, "Black")
        
    player.draw(canvas, [50, 400])

    
# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)


# get things rolling
deal()
frame.start()

