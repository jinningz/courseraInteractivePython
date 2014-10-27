# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import simplegui
import random
import math

number_range = 100



# helper function to start and restart the game
def new_game():
    # initialize global variables used in your code here
    global secret_number, number_range, number_guesses, max_guesses
    
    max_guesses = math.ceil(math.log(number_range, 2))
    number_guesses = 1
    print ""
    print "New game. Range is from 0 to", number_range
    print "Number of remaining guesses is ", int(max_guesses)
    secret_number = random.randrange(0, number_range)



# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    global secret_number, number_range

    number_range = 100
    new_game()


def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    global secret_number, number_range

    number_range = 1000
    new_game()
    
def input_guess(guess):
    # main game logic goes here	
    global secret_number, number_guesses, max_guesses

    guess = int(guess)
    print ""
    print "Guess was ", guess 
    print "Number of remaining guesses is ", int(max_guesses - number_guesses)
    
    if number_guesses < max_guesses:
        
        if guess < secret_number:
            print "Higher!"
        elif guess > secret_number:
            print "Lower!"
        else:
            print "Correct!"
            new_game()
            
        number_guesses += 1
    else:
        if guess == secret_number:
            print "Correct!"
        else:
            print "You ran out of guesses.  The number was", secret_number
        new_game()

    
# create frame
f = simplegui.create_frame("Guess the number", 200, 200)

# register event handlers for control elements and start frame

f.add_button("Range is [0, 100)", range100, 200)
f.add_button("Range is [0, 1000)", range1000, 200)
f.add_button("Restart game", new_game)
inp = f.add_input('Enter a guess', input_guess, 50)


# call new_game 
new_game()


# always remember to check your completed program against the grading rubric
