from os import fdopen

import random
import sys
import json

def createMaze(width, height):
    """Creates a maze using recursive backtracking."""
    maze = [['1'] * width for _ in range(height)]  # Initialize maze with walls

    def dfs(x, y):
        maze[y][x] = '0'  # Mark current cell as path
        directions = [(0, 2), (2, 0), (0, -2), (-2, 0)]  # Possible directions to move
        random.shuffle(directions)  # Randomize direction order

        for dx, dy in directions:
            nx, ny = x + dx, y + dy  # Calculate new cell coordinates
            if 0 < nx < width - 1 and 0 < ny < height - 1 and maze[ny][nx] == '1':
                maze[y + dy // 2][x + dx // 2] = '0'  # Carve path
                dfs(nx, ny)  # Recursively call DFS on new cell

    # Ensure odd dimensions for proper maze generation
    start_x, start_y = 1, 1
    dfs(start_x, start_y)
    maze[start_y][start_x] = '0' ###S
    maze[height - 2][width - 2] = '0' ###E

    output = ""
    #output1 = ""
    for row in maze:
        output = output + ''.join(row)
        #for v in row:
         #   output1 = output1 + v + ","
        #output1 = output1 + "\n"

    return output

def fixMaze(width, height, maze, name):
    i: int = 0

    data = []
    newData = []
    for y in range(height):
        data.append([])
        newData.append([])
        for x in range(width):
            data[y].append(int(maze[i]))
            newData[y].append(int(maze[i]))
            i = i + 1

    newData[0][0] = 2
    newData[0][width - 2] = 3

    for y in range(1, height - 1):
        for x in range(1, width - 1):
            if data[y][x] == 0 and data[y][x - 1] == 1 and data[y][x + 1] == 0 and data[y - 1][x] == 1 and data[y + 1][x] == 0:
                newData[y][x] = 8
                continue
            if data[y][x] == 0 and data[y][x - 1] == 0 and data[y][x + 1] == 1 and data[y - 1][x] == 1 and data[y + 1][x] == 0:
                newData[y][x] = 9
                continue
            if data[y][x] == 0 and data[y][x - 1] == 1 and data[y][x + 1] == 0 and data[y - 1][x] == 0 and data[y + 1][x] == 1:
                newData[y][x] = 11
                continue
            if data[y][x] == 0 and data[y][x - 1] == 0 and data[y][x + 1] == 1 and data[y - 1][x] == 0 and data[y + 1][x] == 1:
                newData[y][x] = 12
                continue
            if data[y][x] == 0 and data[y][x - 1] == 0 and data[y][x + 1] == 0 and data[y - 1][x] == 0 and data[y + 1][x] == 1:
                newData[y][x] = 13
                continue
            if data[y][x] == 0 and data[y][x - 1] == 1 and data[y][x + 1] == 0 and data[y - 1][x] == 0 and data[y + 1][x] == 0:
                newData[y][x] = 14
                continue
            if data[y][x] == 0 and data[y][x - 1] == 0 and data[y][x + 1] == 1 and data[y - 1][x] == 0 and data[y + 1][x] == 0:
                newData[y][x] = 15
                continue
            if data[y][x] == 0 and data[y][x - 1] == 0 and data[y][x + 1] == 0 and data[y - 1][x] == 1 and data[y + 1][x] == 0:
                newData[y][x] = 16
                continue
            if data[y][x] == 0 and data[y][x - 1] == 0 and data[y][x + 1] == 0 and data[y - 1][x] == 0 and data[y + 1][x] == 0:
                newData[y][x] = 17
                continue
            if data[y][x] == 0 and data[y][x - 1] == 1 and data[y][x + 1] == 1:
                newData[y][x] = 6
                continue

            if data[y][x] == 1 and data[y][x - 1] == 0 and data[y][x + 1] == 1 and data[y - 1][x] == 0 and data[y + 1][x] == 1:
                newData[y][x] = 2
                continue
            if data[y][x] == 1 and data[y][x - 1] == 1 and data[y][x + 1] == 0 and data[y - 1][x] == 0 and data[y + 1][x] == 1:
                newData[y][x] = 3
                continue
            if data[y][x] == 1 and data[y][x - 1] == 1 and data[y][x + 1] == 0 and newData[y - 1][x] == 4:# and data[y + 1][x] == 0:
                newData[y][x] = 18
                continue
            if data[y][x] == 1 and data[y][x - 1] == 0 and data[y][x + 1] == 1 and newData[y - 1][x] == 5:# and data[y + 1][x] == 0:
                newData[y][x] = 19
                continue
            if data[y][x] == 1 and data[y][x - 1] == 0 and data[y][x + 1] == 1 and newData[y - 1][x] == 4 and data[y + 1][x] == 0:
                newData[y][x] = 1
                continue

            if data[y][x] == 1 and data[y][x - 1] == 0 and (newData[y - 1][x] == 2 or newData[y - 1][x] == 4):
                newData[y][x] = 4
                continue
            if data[y][x] == 1 and data[y][x - 1] == 0 and (newData[y - 1][x] == 3 or newData[y - 1][x] == 5):
                newData[y][x] = 5
                continue


    for y in range(1, height - 1):
       for x in range(1, width - 0):
          if newData[y][x] == 1 and newData[y + 1][x] == 1:
             newData[y][x] = 4

    for y in range(height - 1):
        for x in range(width - 1):
            if newData[y][x] == 4 and newData[y][x + 1] == 1:
                newData[y][x] = 2
                continue
            if newData[y][x] == 1 and newData[y + 1][x] == 4:
                newData[y][x] = 2
                continue
            if newData[y][x] == 1 and data[y][x + 1] == 0 and data[y][x - 1] == 0 and data[y + 1][x] == 0:
                newData[y][x] = newData[y - 1][x]
                continue
            if newData[y][x] == 18 and newData[y + 1][x] == 4:
                newData[y][x] = 4
                continue
            if newData[y][x] == 19 and newData[y + 1][x] == 4:
                newData[y][x] = 2
                continue
            if newData[y][x] == 5 and newData[y + 1][x] == 4:
                newData[y][x] = 2
                continue

            if data[y][x] == 1 and data[y][x - 1] == 1 and data[y][x + 1] == 0 and newData[y - 1][x] == 4 and data[y + 1][x] == 0:
                newData[y][x] = 18
                continue
            if data[y][x] == 1 and data[y][x - 1] == 0 and data[y][x + 1] == 1 and newData[y - 1][x] == 5 and data[y + 1][x] == 0:
                newData[y][x] = 19
                continue

    for y in range(1, height - 1):
       for x in range(1, width - 1):
          if newData[y][x] == 0:
             newData[y][x] = 7

    for y in range(1, height):
        if newData[y][1] == 1:
            newData[y][0] = 2
        else:
            newData[y][0] = 4

    for y in range(1, height):
        if newData[y][width - 3] == 1:
            newData[y][width - 2] = 3
        else:
            newData[y][width - 2] = 5

    for x in range(width):
        newData[height - 2][x] = 1

    #open paths
    for y in range(1, height - 1):
       for x in range(1, width - 1):
           #continue
           if (newData[y][x] == 4 and random.randint(1, 4) == 2 and
            newData[y - 1][x] == 4 and data[y - 1][x + 1] == 0 and data[y - 1][x - 1] == 0 and
            newData[y + 1][x] == 4 and data[y + 1][x + 1] == 0 and data[y + 1][x - 1] == 0 and
            data[y][x - 1] == 0 and data[y][x + 1] == 0):
                data[y][x] = 0
                newData[y][x] = 7
                newData[y][x - 1] = 14
                newData[y][x + 1] = 15
                continue
           if (newData[y][x] == 1 and random.randint(1, 4) == 2 and
            newData[y][x - 1] == 1 and data[y - 1][x - 1] == 0 and data[y + 1][x - 1] == 0 and
            newData[y][x + 1] == 1 and data[y - 1][x + 1] == 0 and data[y + 1][x + 1] == 0 and
            data[y - 1][x] == 0 and data[y + 1][x] == 0):
                data[y][x] = 0
                newData[y][x] = 6
                newData[y - 1][x] = 16
                newData[y + 1][x] = 13
                continue

    #Fix paths
    for y in range(1, height - 1):
        for x in range(1, width - 1):
            #continue
            if data[y][x] == 0 and data[y][x - 1] == 0 and data[y][x + 1] == 0 and data[y - 1][x] == 0 and data[y + 1][x] == 1:
                newData[y][x] = 13
                continue
            if data[y][x] == 0 and data[y][x - 1] == 1 and data[y][x + 1] == 0 and data[y - 1][x] == 0 and data[y + 1][x] == 0:
                newData[y][x] = 14
                continue
            if data[y][x] == 0 and data[y][x - 1] == 0 and data[y][x + 1] == 1 and data[y - 1][x] == 0 and data[y + 1][x] == 0:
                newData[y][x] = 15
                continue
            if data[y][x] == 0 and data[y][x - 1] == 0 and data[y][x + 1] == 0 and data[y - 1][x] == 1 and data[y + 1][x] == 0:
                newData[y][x] = 16
                continue
            if data[y][x] == 0 and data[y][x - 1] == 0 and data[y][x + 1] == 0 and data[y - 1][x] == 0 and data[y + 1][x] == 0:
                newData[y][x] = 17
                continue

    output = ""
    output1 = ""
    for y in range(height):
        for x in range(width):
            output = output + str(newData[y][x]) + ","
            output1 = output1 + str(newData[y][x]) + ","
        output = output + "\n"

    f = open("res\\mazeTemplate.json")
    m = f.read()
    m = m.replace("@width", str(width))
    m = m.replace("@height", str(height))
    m = m.replace("@maze", output.strip().strip(","))
    f.close()

    f = open("res\\" + name + ".data", "w")
    f.write(output1.strip().strip(","))
    f.close()

    f = open("res\\" + name, "w")
    f.write(m)
    f.close()

def createFinalMaze(name: str):
    data = json.load(open("res\\" + name))

    #maze = ""
    enemies = ""
    rods = ""
    altars = ""
    exit =""

    index: int = 0
    for value in data["layers"][0]["data"]:
        if value == 21:
            altars = altars + str(index) + ","
        if value == 91:
            enemies = enemies + str(index) + ","
        if value == 93:
            rods = rods + str(index) + ","
        if value == 92:
            exit = str(index)

        index = index + 1
        #maze = maze + str(value) + ","

    mazeData = {}
    mazeData["width"] = data["width"]
    mazeData["height"] = data["height"]
    mazeData["tileSize"] = data["tilewidth"]
    mazeData["colliders"] = "1,2,3,4,5,18,19"

    mazeData["enemies"] = enemies.strip(",")
    mazeData["enemyDefeatOrder"] = "1,2,3,4"
    mazeData["altars"] = altars.strip(",")
    mazeData["rods"] = rods.strip(",")
    mazeData["exit"] = exit

    f = open("res\\" + name + ".data")
    mazeData["data"] = f.read()
    f.close()

    f = open("mazes\\" + name.rstrip(".tmj") + ".json", "w")
    f.write(json.dumps(mazeData, indent = 4))
    f.close()

if __name__ == "__main__":
    sys.setrecursionlimit(30000)

    width = 200
    height = 200

    #for i in range(10):
     #   maze = createMaze(width, height)
      #  fixMaze(width, height, maze, "maze" + str(i + 1) + ".tmj")

    createFinalMaze("maze1.tmj")