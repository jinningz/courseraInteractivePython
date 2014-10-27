# Implementation of classic arcade game Pong

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False # Constant
RIGHT = True # Constant

# Initialize ball position and velocity
ball_pos = [WIDTH / 2, HEIGHT / 2]
ball_vel = [0, 0]

# paddle1_pos and paddle2_pos are defined as the relative distance between
# the top left corner of the paddle and the top wall
paddle1_pos = HEIGHT / 2 - PAD_HEIGHT / 2
paddle2_pos = HEIGHT / 2 - PAD_HEIGHT / 2
paddle1_vel = 0
paddle2_vel = 0

# Initialize scores
score1 = 0
score2 = 0


# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists

    ball_pos = [WIDTH / 2, HEIGHT / 2]
    
    # Randomize vertical speed
    v_vel = random.randrange(120, 240) / 60.0
    # Randomize horizontal speed
    h_vel = random.randrange(60, 180) / 60.0
    
    # whether direction is RIGHT == True
    if direction:
        ball_vel = [h_vel, -v_vel]
    else:
        ball_vel = [-h_vel, -v_vel]
    
    

# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints

    # Randomize initial ball direction LEFT / RIGHT
    spawn_ball(random.choice([LEFT, RIGHT]))
    
    score1 = 0
    score2 = 0
    
    
def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel

    # Define behaviour when ball hit the top or bottom walls
    if (ball_pos[1] <= BALL_RADIUS) or (ball_pos[1] >= HEIGHT - BALL_RADIUS - 1):
        ball_vel[1] = -ball_vel[1]

    # Tests if the ball touches the left gutters or paddle
    # Player 2 wins
    if ball_pos[0] <= PAD_WIDTH + BALL_RADIUS:
        if paddle1_pos <= ball_pos[1] <= paddle1_pos + PAD_HEIGHT:
            ball_vel[0] = -ball_vel[0] * 1.1
            ball_vel[1] = ball_vel[1] * 1.1
        else:
            score2 += 1
            spawn_ball(RIGHT)
    
    # Tests if the ball touches the right gutters or paddle
    # Player 1 wins
    if ball_pos[0] >= WIDTH - PAD_WIDTH - BALL_RADIUS - 1: 
        if paddle2_pos <= ball_pos[1] <= paddle2_pos + PAD_HEIGHT:
            ball_vel[0] = -ball_vel[0] * 1.1
            ball_vel[1] = ball_vel[1] * 1.1
        else:
            score1 += 1
            spawn_ball(LEFT)
    
    
        
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
        
    # update ball
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
    
    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 2, "White", "White")
    
    # update paddle's vertical position, keep paddle on the screen
    
    if (paddle1_pos + paddle1_vel >= 0) and (paddle1_pos + paddle1_vel <= HEIGHT - PAD_HEIGHT):
        paddle1_pos += paddle1_vel
    if (paddle2_pos + paddle2_vel >= 0) and (paddle2_pos + paddle2_vel <= HEIGHT - PAD_HEIGHT):
        paddle2_pos += paddle2_vel
    
    
    
    # draw paddles
    # paddle1_pos is the relative location of top left corner of paddle1
    # which is the vertical distance between the top wall 
    # and top left corner of paddle1
    # paddle2_pos is the vertical distance between the top wall 
    # and top left corner of paddle2
    
    # The paddle polygon is drawn in relative position to the reference point, 
    # which is paddle#_pos.
    canvas.draw_polygon([[0, paddle1_pos], 
                          [PAD_WIDTH, paddle1_pos], 
                          [PAD_WIDTH, paddle1_pos + PAD_HEIGHT], 
                          [0, paddle1_pos + PAD_HEIGHT],
                          [0, paddle1_pos]],
                          1, "White", "White")
    canvas.draw_polygon([[WIDTH - PAD_WIDTH, paddle2_pos], 
                          [WIDTH, paddle2_pos], 
                          [WIDTH, paddle2_pos + PAD_HEIGHT], 
                          [WIDTH - PAD_WIDTH, paddle2_pos + PAD_HEIGHT],
                          [WIDTH - PAD_WIDTH, paddle2_pos]],
                          1, "White", "White")
    
    # draw scores
    canvas.draw_text(str(score1), [200, 75], 50, "White")
    canvas.draw_text(str(score2), [380, 75], 50, "White")

    
def keydown(key):
    # When a key is pressed
    global paddle1_vel, paddle2_vel
    
    if key == simplegui.KEY_MAP['w']:
        paddle1_vel = -5
    if key == simplegui.KEY_MAP['s']:
        paddle1_vel = 5       
    if key == simplegui.KEY_MAP['up']:
        paddle2_vel = -5   
    if key == simplegui.KEY_MAP['down']:
        paddle2_vel = 5 

   
def keyup(key):
    # when a key is released
    global paddle1_vel, paddle2_vel

    paddle1_vel = 0
    paddle2_vel = 0
    
    
# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button("Restart", new_game, 75)

# start frame
new_game()
frame.start()
