import pygame
from grid import *

pygame.init()

# variables
white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)

X = 900
Y = 650 

# Define screen
screen = pygame.display.set_mode((X, Y))

# Define Array that saves positions
rectPos = []

# Function that draws Grid on the screen
def boxes(row):
    posY = (Y // len(grid) // 1.5)
    posX = (X // len(grid[0]) // 1.5)
    for i in range(0, len(grid[row])):
        pos = [(i+1)*posX, (row+1)*posY]
        box = pygame.Rect(pos[0], pos[1], (X // len(grid[0]) // 1.5 * 0.9), (Y // len(grid) // 1.5 * 0.9))
        margin = pygame.Rect((i+1)*posX, (row+1)*posY, (X // len(grid[0]) // 1.5), (Y // len(grid)) // 1.5 )
        rectPos.append(box)
        pygame.draw.rect(screen, white, margin)
        pygame.draw.rect(screen, green, box)

# Function that draws the hidden number of a gridbox using the input from a left-click
# argument - Function inputs a pygame.Rect value that is used to determine which gridbox 
# that is going to show its hidden number
# return - Doesn't exist
def numbers(position):
    posY = (Y // len(grid) // 1.5)
    posX = (X // len(grid[0]) // 1.5)
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            pos = [(j+1)*posX, (i+1)*posY]
            if position == pygame.Rect(pos[0], pos[1], (X // len(grid[0]) // 1.5 * 0.9), (Y // len(grid) // 1.5 * 0.9)):
                #Define font
                font = pygame.font.Font('freesansbold.ttf', (X // len(grid[0]) // 4))
                gridText = str(grid[i][j])
                text = font.render(gridText, True, blue)
                screen.blit(text, position)

# Function that draws green boxes to cover the number on the pre-existed box
# argument - inputs 2 Rect-classes, which looks like this: rect<x, y, width, height> where all values
# inside the rect are integers. The inputs are used to draw the green boxes on correct positions with
# correct sizing.
# return - Doesn't exist
def fel(pos1, pos2):
    pygame.draw.rect(screen, green, pos1)
    pygame.draw.rect(screen, green, pos2)

# Function that finds the correct number for the gridbox position from input and returns it
# argument - The input is a Rect-class that is used with a comparison operator to find which row
# and row-position the hidden number is at. 
# return - integer - Value of the hidden number
def gridNumber(position):
    posY = (Y // len(grid) // 1.5)
    posX = (X // len(grid[0]) // 1.5)
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            pos = [(j+1)*posX, (i+1)*posY]
            if position == pygame.Rect(pos[0], pos[1], (X // len(grid[0]) // 1.5 * 0.9), (Y // len(grid) // 1.5 * 0.9)):
                number = grid[i][j]
                return number

# Function that uses the input variables to draw the amount of rights, wrongs and rounds of the game
# argument - 3 integer values that are used to draw the correct number for each counter.
# return - doesn't exist
def score(wrongs, rounds, rights):
    # Creates the text positions
    rect1 = pygame.Rect(X // 8 * 3.2, 0.5, 2, 3)
    rect2 = pygame.Rect(X // 8 * 5.5, 0.5, 2, 3)
    rect3 = pygame.Rect(X // 8, 0.5, 2, 3)
    # define font-variable used to render text
    font = pygame.font.Font('freesansbold.ttf', X // 20)
    # variables containing strings with the value of the input variables as a string
    roundsText = "Rounds:" + str(rounds)
    wrongsText = "Wrongs:" + str(wrongs)
    rightsText = "Rights:" + str(rights)
    # 3 string-variables containing rendered forms of the text variables.
    text1 = font.render(roundsText, True, blue)
    text2 = font.render(wrongsText, True, blue)
    text3 = font.render(rightsText, True, blue)
    # Draws a white rectangle box on top of the counters to reset the value
    pygame.draw.rect(screen, white, pygame.Rect(X // 8, 0.5, X, 40))
    # Draws the text on the rect position
    screen.blit(text1, rect1)
    screen.blit(text2, rect2)
    screen.blit(text3, rect3)
