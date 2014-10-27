
import math, random

def name_to_number(name):
    if name == 'rock':
        number = 0
    elif name == 'Spock':
        number = 1
    elif name == 'paper':
        number = 2
    elif name == 'lizard':
        number = 3
    elif name == 'scissors':
        number = 4
    else:
        number = -9999
        print 'Invalid input: name'
    return number

def number_to_name(number):
    if number == 0:
        name = 'rock'
    elif number == 1:
        name = 'Spock'
    elif number == 2:
        name = 'paper'
    elif number == 3:
        name = 'lizard'
    elif number == 4:
        name = 'scissors'
    else:
        name = 'NA'
        print 'Invalid input: number'
    return name

def rpsls(player_choice):
    print ''
    print 'Player chooses ' + player_choice
    player_number = name_to_number(player_choice)
    #print 'player_number ' + str(player_number)
    
    
    comp_number = random.randrange(5)
    comp_choice = number_to_name(comp_number)
    print 'Computer chooses ' + comp_choice
    #print 'comp_number ' + str(comp_number)
    
    pvc = (comp_number - player_number) % 5
    #print pvc
    
    if pvc == 0:
        print 'Player and computer tie!'
    elif (pvc == 1) or (pvc == 2):
        print 'Computer wins!'
    elif (pvc == 3) or (pvc == 4):
        print 'Player wins!'
    else:
        print 'Invalid'
    
# Testing
rpsls('rock')
rpsls('Spock')
rpsls('paper')
rpsls('lizard')
rpsls('scissors')

