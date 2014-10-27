# "Stopwatch: The Game"

import simplegui
import math

# define global variables
t = 0 # time in tens of seconds
status = False # Whether the watch is running
numStopped = 0 # Number of times the Stop button was clicked
numWhole = 0 # Number of times stopped at whole second


# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    
    # Format a:bc.d
    a = int(math.floor(t/600)) # Minute
    sec = int(math.floor((t - 600*a)/10)) # Second
    # First character of second
    if (sec < 10):
        b = "0"
    else:
        b = str(sec)[0]
    c = str(sec)[-1] # 2nd character of second
    d = t % 10 # tens of seconds
    
    # Update global variable
    return str(a) + ":" + b + c + "." + str(d)
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start_button():
    global status
    timer.start()
    status = True
    
def stop_button():
    global t, status, numStopped, numWhole
    timer.stop()
    
    # Accumulate game counter (only when game is running)
    if (status == True):
        numStopped += 1

        if (t % 10 == 0):
            numWhole += 1
        
        #print ""
        #print "Timer ", t_str
        #print "Stop button clicked ", numStopped
        #print "Times stopped at whole second ", numWhole
     
    status = False
    
def reset_button():
    global status, t, numStopped, numWhole
    timer.stop()
    
    # Reset all global variables
    t = 0 
    status = False
    numStopped = 0
    numWhole = 0

# define event handler for timer with 0.1 sec interval
def tick():
    global t
    t += 1 # Counter!

# define draw handler
def draw(canvas):
    global t, numStopped, numWhole
    
    g_str = str(numWhole) + "/" + str(numStopped)
    
    canvas.draw_text(format(t), [95, 120], 50, "White")
    canvas.draw_text(g_str, [225, 40], 35, "Green")
    
# create frame
frame = simplegui.create_frame("Timer", 300, 200)

# register event handlers
frame.set_draw_handler(draw)
timer = simplegui.create_timer(100, tick)
frame.add_button("Start", start_button, 75)
frame.add_button("Stop", stop_button, 75)
frame.add_button("Reset", reset_button, 75)

# start frame
frame.start()


# Please remember to review the grading rubric
