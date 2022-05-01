import numpy as np

class cube:
    def __init__(self, cube=None):
        if not cube:
            self.cube = None
        else:
            self.cube = cube

    def newCube(self): # 3*3*3 cube
        cube = []
        for i in range(1, 7):
            cube.append(np.full((3, 3), i))
        
        #test
        
        cube[0] = np.array(([1, 2, 3], [4, 5, 6], [7, 8, 9]))
        cube[1] = np.array(([1, 2, 3], [4, 5, 6], [7, 8, 9]))
        cube[2] = np.array(([1, 2, 3], [4, 5, 6], [7, 8, 9]))
        cube[3] = np.array(([1, 2, 3], [4, 5, 6], [7, 8, 9]))
        cube[4] = np.array(([1, 2, 3], [4, 5, 6], [7, 8, 9]))
        cube[5] = np.array(([1, 2, 3], [4, 5, 6], [7, 8, 9]))

        self.cube = cube

    def showCube(self, color=True):
        floorPlan = np.zeros((9, 12))
        floorPlan[3:6, 3:6] = self.cube[0]
        floorPlan[3:6, 6:9] = self.cube[1]
        floorPlan[3:6, 9:12] = self.cube[2]
        floorPlan[3:6, 0:3] = self.cube[3]
        floorPlan[0:3, 3:6] = self.cube[4]
        floorPlan[6:9, 3:6] = self.cube[5]

        floorPlan = floorPlan.tolist()

        for i in floorPlan:
            for v in i:
                if color:
                    if v == 0:
                        colorCode = 30
                    elif v == 1:
                        colorCode = 37
                    elif v == 2:
                        colorCode = 34
                    elif v == 3:
                        colorCode = 33
                    elif v == 4:
                        colorCode = 32
                    elif v == 5:
                        colorCode = 91
                    elif v == 6:
                        colorCode = 31
                    else:
                        colorCode = 90

                else:
                    colorCode = 0

                print(f"\033[{colorCode}m{int(v)}\033[0m. ", end="")
            print("")

    def up(self, prime=False, count=1):
        for _ in range(count):
            cube = np.array(self.cube, copy=True)
            if prime:
                cube[4] = np.rot90(self.cube[4])

                cube[0][0] = self.cube[3][0]
                cube[1][0] = self.cube[0][0]
                cube[2][0] = self.cube[1][0]
                cube[3][0] = self.cube[2][0]

            else:
                cube[4] = np.rot90(self.cube[4], -1)

                cube[0][0] = self.cube[1][0]
                cube[1][0] = self.cube[2][0]
                cube[2][0] = self.cube[3][0]
                cube[3][0] = self.cube[0][0]

            self.cube = np.array(cube, copy=True)

    def down(self, prime=False, count=1):
        for _ in range(count):
            cube = np.array(self.cube, copy=True)
            if prime:
                cube[5] = np.rot90(self.cube[5], -1)
                cube[0][2] = self.cube[3][2]
                cube[1][2] = self.cube[0][2]
                cube[2][2] = self.cube[1][2]
                cube[3][2] = self.cube[2][2]

            else:
                cube[5] = np.rot90(self.cube[5])
                cube[0][2] = self.cube[1][2]
                cube[1][2] = self.cube[2][2]
                cube[2][2] = self.cube[3][2]
                cube[3][2] = self.cube[0][2]


            self.cube = np.array(cube, copy=True)

    def doubleUp(self, prime=False, count=1):
        for _ in range(count):
            cube = np.array(self.cube, copy=True)
            if prime:
                cube[4] = np.rot90(self.cube[4])

                cube[0][:2] = self.cube[3][:2]
                cube[1][:2] = self.cube[0][:2]
                cube[2][:2] = self.cube[1][:2]
                cube[3][:2] = self.cube[2][:2]

            else:
                cube[4] = np.rot90(self.cube[4], -1)

                cube[0][:2] = self.cube[1][:2]
                cube[1][:2] = self.cube[2][:2]
                cube[2][:2] = self.cube[3][:2]
                cube[3][:2] = self.cube[0][:2]

            self.cube = np.array(cube, copy=True)

    def doubleDown(self, prime=False, count=1):
        for _ in range(count):
            cube = np.array(self.cube, copy=True)
            if prime:
                cube[5] = np.rot90(self.cube[5], -1)
                cube[0][1:3] = self.cube[3][1:3]
                cube[1][1:3] = self.cube[0][1:3]
                cube[2][1:3] = self.cube[1][1:3]
                cube[3][1:3] = self.cube[2][1:3]

            else:
                cube[5] = np.rot90(self.cube[5])
                cube[0][1:3] = self.cube[1][1:3]
                cube[1][1:3] = self.cube[2][1:3]
                cube[2][1:3] = self.cube[3][1:3]
                cube[3][1:3] = self.cube[0][1:3]


            self.cube = np.array(cube, copy=True)

    def front(self, prime=False, count=1):
        for _ in range(count):
            cube = np.array(self.cube, copy=True)
            if prime:
                cube[0] = np.rot90(self.cube[0])

                cube[1][:, 0] = self.cube[5][0][::-1]
                cube[5][0] = self.cube[3][:, 2]
                cube[3][:, 2] = self.cube[4][2][::-1]
                cube[4][2] = self.cube[1][:, 0]

            else:
                cube[0] = np.rot90(self.cube[0], -1)

                cube[1][:, 0] = self.cube[4][2]
                cube[5][0] = self.cube[1][:, 0][::-1]
                cube[3][:, 2] = self.cube[5][0]
                cube[4][2] = self.cube[3][:, 2][::-1]

            self.cube = np.array(cube, copy=True)

    def doubleFront(self, prime=False, count=1):
        for _ in range(count):
            cube = np.array(self.cube, copy=True)
            if prime:
                cube[0] = np.rot90(self.cube[0])

                cube[1][:, :2] = np.rot90(self.cube[5][:2])
                cube[5][:2] = np.rot90(self.cube[3][:, 1:])
                
                cube[3][:, 1:] = np.rot90(self.cube[4][1:])
                cube[4][1:] = np.rot90(self.cube[1][:, :2])


            else:
                cube[0] = np.rot90(self.cube[0], -1)

                cube[1][:, :2] = np.rot90(self.cube[4][1:], -1)
                cube[5][:2] = np.rot90(self.cube[1][:, :2], -1)
                
                cube[3][:, 1:] = np.rot90(self.cube[5][:2], -1)
                cube[4][1:] = np.rot90(self.cube[3][:, 1:], -1)

            self.cube = np.array(cube, copy=True)


if __name__ == "__main__":
    myCube = cube()
    myCube.newCube()

    myCube.showCube()
    print("")
    myCube.doubleFront(prime=True)
    myCube.showCube()