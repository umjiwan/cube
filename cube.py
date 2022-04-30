import numpy as np

def createCube():
    cube = []
    for i in range(1, 7):
        cube.append(np.full(((3, 3)), i))

    return cube

def printFloorPlan(cube):
    floorPlan = np.zeros((9, 12))
    floorPlan[3:6, 3:6] = cube[0]
    floorPlan[3:6, 6:9] = cube[1]
    floorPlan[3:6, 9:12] = cube[2]
    floorPlan[3:6, 0:3] = cube[3]
    
    floorPlan[0:3, 3:6] = cube[4]
    floorPlan[6:9, 3:6] = cube[5]

    print(floorPlan)

def up(cube):
    _cube = cube[:]
    _cube[0] = 1
    printFloorPlan(_cube)

cube = createCube()
up(cube)



