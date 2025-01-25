# my attempt to create a random map
from random import randint

"""
increment is size of a square on the grid (100 pixels?)
start is position player character will start in 
end is position he needs to end up
max is border: bottom-rightmost position 
Use EXACT pixel values for all (measured from 
origin at top right (0, 0))
"""
def createRandomPath(x_start, y_start, x_end, y_end, x_max, y_max, increment):
    entireBoard = list(range(x_max / increment))
    for column in entireBoard:
        entireBoard[column] = list(range(y_max / increment))

    map_start = [x_start, y_start]
    map_end = [x_end, y_end]
    map_corner = [(x_max - increment), (y_max - increment)]

    currXY = map_start

    # directions are going to be like a clock
    # 1 is up, 2 is right, 3 is down, 4 is left
    while (currXY != map_end):
        nextPos = randint(1, 4)
        if nextPos == 1:
            if (currXY[1] - increment) >= 0:


