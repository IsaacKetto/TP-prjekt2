from random import shuffle, randrange
import math

#Input variable for pairs and defines card_amount variable
pair_amount = int(input("Enter the amount of pairs: "))
card_amount = pair_amount * 2

#take out height
grid_height = 1
for i in range(math.floor(math.sqrt(card_amount)), 1, -1):
    if card_amount % i == 0:
        grid_height = i
        break
    
#Defines grid_width variable and its content
grid_width = card_amount // grid_height


#Creates an Array containing every number required and shuffles them
hidden_numbers = list(range(1, pair_amount + 1)) * 2
shuffle(hidden_numbers)

#Creates 2 variables, the grid variable for the layout and the hidden_number_iter used to append
#rows to the grid Array
hidden_number_iter = iter(hidden_numbers)
grid = []

# Generate the grid
for y in range(grid_height):
    row = [next(hidden_number_iter) for x in range(grid_width)]
    grid.append(row)
    
