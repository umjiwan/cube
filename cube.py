from itertools import count
from turtle import pen
import numpy as np

def createCube():
    cube = []
    for i in range(1, 7):
        cube.append(np.full(((3, 3)), i))

    return cube

def printFloorPlan(cube):
    floorPlan = np.zeros((9, 12)) # init var
    floorPlan[3:6, 3:6] = cube[0] # white
    floorPlan[3:6, 6:9] = cube[1] # blue
    floorPlan[3:6, 9:12] = cube[2] # yellow
    floorPlan[3:6, 0:3] = cube[3] # green
    floorPlan[0:3, 3:6] = cube[4] # orange
    floorPlan[6:9, 3:6] = cube[5] # red

    print(floorPlan)

def up(cube, prime=False, count=1):
    for i in range(count):
        _cube = np.array(cube, copy=True)
        if prime:
            _cube[0][0] = cube[3][0]
            _cube[1][0] = cube[0][0]
            _cube[2][0] = cube[1][0]
            _cube[3][0] = cube[2][0]

            _cube[4] = np.rot90(cube[4])
        else:
            _cube[1][0] = cube[2][0]
            _cube[0][0] = cube[1][0]
            _cube[3][0] = cube[0][0]
            _cube[2][0] = cube[3][0]

            _cube[4] = np.rot90(cube[4], -1)
        cube = np.array(_cube, copy=True)
    return np.array(_cube, copy=True)

def doubleUp(cube, prime=False, count=1):
    for i in range(count):
        _cube = np.array(cube, copy=True)
        
        if prime:
            _cube[0][:2] = cube[3][:2]
            _cube[1][:2] = cube[0][:2]
            _cube[2][:2] = cube[1][:2]
            _cube[3][:2] = cube[2][:2]

            _cube[4] = np.rot90(cube[4])
        else:
            _cube[1][:2] = cube[2][:2]
            _cube[0][:2] = cube[1][:2]
            _cube[3][:2] = cube[0][:2]
            _cube[2][:2] = cube[3][:2]

            _cube[4] = np.rot90(cube[4], -1)
        
        cube = np.array(_cube, copy=True)

    return np.array(_cube, copy=True)

def down(cube, prime=False, count=1):
    for i in range(count):
        _cube = np.array(cube, copy=True)
        
        if prime:
            _cube[0][2] = cube[3][2]
            _cube[1][2] = cube[0][2]
            _cube[2][2] = cube[1][2]
            _cube[3][2] = cube[2][2]

            _cube[5] = np.rot90(cube[5], -1)

        else:
            _cube[1][2] = cube[2][2]
            _cube[0][2] = cube[1][2]
            _cube[3][2] = cube[0][2]
            _cube[2][2] = cube[3][2]

            _cube[5] = np.rot90(cube[5])

        cube = np.array(_cube, copy=True)

    return np.array(_cube, copy=True)

def doubleDown(cube, prime=False, count=1):
    for i in range(count):
        _cube = np.array(cube, copy=True)

        if prime:
            _cube[0][1:3] = cube[3][1:3]
            _cube[1][1:3] = cube[0][1:3]
            _cube[2][1:3] = cube[1][1:3]
            _cube[3][1:3] = cube[2][1:3]

            _cube[5] = np.rot90(cube[5], -1)

        else:
            _cube[1][1:3] = cube[2][1:3]
            _cube[0][1:3] = cube[1][1:3]
            _cube[3][1:3] = cube[0][1:3]
            _cube[2][1:3] = cube[3][1:3]

            _cube[5] = np.rot90(cube[5])

        cube = np.array(_cube, copy=True)
    return np.array(_cube, copy=True)

def front(cube, prime=False, count=1):
    for i in range(count):
        _cube = np.array(cube, copy=True)

        if prime:
            _cube[0] = np.rot90(cube[0])

            _cube[4][2] = np.rot90(cube[1])[2]

            _cube[3] = np.rot90(cube[3])
            _cube[3][0] = cube[4][2]
            _cube[3] = np.rot90(_cube[3], -1)

            _cube[5][0] = np.rot90(cube[3])[0]

            _cube[1] = np.rot90(cube[1])
            _cube[1][2] = cube[5][0]
            _cube[1] = np.rot90(_cube[1], -1)

            
        else:
            _cube[0] = np.rot90(cube[0], -1)
            
            _cube[4][2] = np.rot90(cube[3], -1)[2]

            _cube[1] = np.rot90(cube[1])
            _cube[1][2] = cube[4][2]
            _cube[1] = np.rot90(_cube[1], -1)

            _cube[5][0] = np.rot90(cube[1], -1)[0] 

            _cube[3] = np.rot90(cube[3])
            _cube[3][0] = cube[5][0]
            _cube[3] = np.rot90(_cube[3], -1)

        cube = np.array(_cube, copy=True)

    return np.array(_cube, copy=True)

def countCube(cube):
    for i in range(6):
        print((cube.tolist()).count(i))


cube = createCube()

"""cube[0] = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
cube[1] = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
cube[2] = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
cube[3] = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
cube[4] = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
cube[5] = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])"""
"""
cube = front(cube)
cube = doubleUp(cube)
cube = front(cube, prime=True)
cube = doubleUp(cube, prime=True)

printFloorPlan(cube)
"""
countCube(cube)


