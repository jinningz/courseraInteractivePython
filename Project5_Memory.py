# implementation of card game - Memory

import simplegui
import random

# helper function to initialize globals
def new_game():
    global deck, exposed, state, numTurns, memory
    
    # Initiate deck and shuffle
    deck = range(8) + range(8) 
    random.shuffle(deck)
    
    # The following list stores whether a card is exposed
    exposed = [False]*16
    
    # The following variable stores the state of clicks
    state = 0
    
    numTurns = 0
    
    # The following variable is used to compare exposed cards
    # Squence of card position clicked
    memory = []
 
    
# define event handlers
def mouseclick(pos):
    global exposed, state, numTurns, memory
    
    #print pos
    cardClick = pos[0] // 50
    
    if exposed[cardClick] == False:
        exposed[cardClick] = True
        memory.append(cardClick)
        if state == 0:
            state = 1   
        elif state == 1:
            state = 2
            numTurns += 1
        else:
            state = 1
            if deck[memory[-2]] <> deck[memory[-3]]:
                exposed[memory[-2]] = False
                exposed[memory[-3]] = False      
    
    
# cards are logically 50x100 pixels in size    
def draw(canvas):
    for i in range(len(deck)):

        # Draw cards
        if exposed[i] == True:
            canvas.draw_text(str(deck[i]), (50*(i)+20, 65), 20, "White")
        else:
            canvas.draw_polygon([(50*(i), 0), (50*(i), 100),
                                 (50*(i+1), 100), (50*(i+1), 0)],
                                 1, "Green", "Green")
        
        # Draw borders
        if i <> 0:
            canvas.draw_line((50*i, 0), (50*i, 100), 1, "White")            
        
        label.set_text("Turns = " + str(numTurns))
        label2.set_text("state: card " + str(state))

        
# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")
label2 = frame.add_label("State: card 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()

