# my attempt to create a random map
from random import randint

# from demo import entity

"""
increment is size of a square on the grid (100 pixels?)
start is position player character will start in 
end is position he needs to end up
max is border: bottom-rightmost position 
Use EXACT pixel values for all (measured from 
origin at top right (0, 0))
"""
def createRandomPath(x_start, y_start, x_end, y_end, x_max, y_max, increment, numberOfObstacles):

    # create a board to determine position of obstacles vs walkable paths
    entireBoard = list(range(int(x_max / increment)))
    for column in entireBoard:
        entireBoard[column] = list(range(int(y_max / increment)))

    # map_start = [x_start, y_start]
    map_end = [x_end, y_end]
    # map_corner = [(x_max - increment), (y_max - increment)]

    currXY = [x_start, y_start]

    # directions are going to be like a clock
    # 1 is up, 2 is right, 3 is down, 4 is left
    while (currXY != map_end):
        nextPos = randint(1, 4)
        if nextPos == 1:
            if (currXY[1] - increment) >= 0:
                entireBoard[currXY[0], currXY[1] - increment] = True
        if nextPos == 2:
            if (currXY[0] + increment) <= y_max:
                entireBoard[currXY[0], currXY[1] + increment] = True
        if nextPos == 3:
            if (currXY[1] + increment) <= x_max:
                entireBoard[currXY[0], currXY[1] + increment] = True
        if nextPos == 4:
            if (currXY[0] - increment) >= 0:
                entireBoard[currXY[0], currXY[1] - increment] = True
    # fill board in with specified number of obstacles
    for i in range(numberOfObstacles):
        random_x = x_start
        random_y = y_start
        while random_x != True and random_y != True:
            random_x = randint(0, int(x_max / increment))
            random_y = randint(0, int(y_max / increment))
        entireBoard[random_x, random_y] = False
    return entireBoard


if __name__ == '__main__':
    board = createRandomPath(0, 0, 10, 10, 10, 10, 1, 5)
    print(board)

