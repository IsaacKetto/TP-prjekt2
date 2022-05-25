import pygame
from grid import *
from functions import boxes, rectPos, numbers, fel, gridNumber, score

pygame.init()

# Colors, width and height
white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)

X = 900
Y = 650 

#  set the screen
screen = pygame.display.set_mode((X, Y))

# choose background color
background_colour = white
 
# Set window name
pygame.display.set_caption("Memory Game")

# Fill background with background_colour
screen.fill(background_colour)

# Update window
pygame.display.flip()

# For-loop that starts function boxes()    
for row in range(len(grid)):
    boxes(row)

# Variable to keep window running
running = True

# Variable to count guesses
guesses = 0

# Variables to count wrongs, rights and rounds
rounds = 0
rights = 0
wrongs = 0

# Variables that is used to display rights, wrongs and rounds
roundstext = ""
rightsText = ""
wrongsText = ""

# 2 variables that saves mouse positions when left-mouse button is pressed
pos1 = 0
pos2 = 0

# Game loop
while running: 

# For loop through the event queue
    for event in pygame.event.get():
        
        # Check for QUIT event
        if event.type == pygame.QUIT:
            running = False
        
        # Check for mouse press on Grid boxes
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                for pos in rectPos:
                    if (pos.collidepoint(pygame.mouse.get_pos())):
                        # shows the hidden number on the colliding box and increases guesses with 1
                        numbers(pos)
                        guesses += 1
                        pygame.display.update()
                        # checks if 2 guesses has been made where even numbers equals 2 guesses
                        if guesses%2 != 0:
                            # Saves position
                            pos1 = pos
                            number1 = gridNumber(pos)
                        elif guesses%2 == 0:
                            pos2 = pos
                            number2 = gridNumber(pos)
                            # Delays algoritm to let player see the second number
                            pygame.time.delay(1000)
                            # Checks if the two numbers are equal to each other
                            if number1 == number2:
                                rights += 1
                                rounds += 1
                                # Function that draws scores for the game, including wrongs, rights and rounds
                                score(wrongs, rounds, rights)
                            else:
                                wrongs += 1
                                rounds += 1
                                score(wrongs, rounds, rights)
                                # Function that redraws the boxes
                                fel(pos1, pos2)
    # Checks if all numbers have been found and changes the running variable to False
    # to end the infinite loop
    if rights == pair_amount:
        running = False 

    # Updates the display to show all the changes that have occured
    pygame.display.update()
            
