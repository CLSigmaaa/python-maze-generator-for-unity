import random

def checkNeighbors(maze, cellCoordinates):
    res = []
    if cellCoordinates[0] > 0:
        res.append((cellCoordinates[0] - 1, cellCoordinates[1]))
    elif cellCoordinates[0] == 0:
        res.append(None)
    if cellCoordinates[0] < len(maze) - 1:
        res.append((cellCoordinates[0] + 1, cellCoordinates[1]))
    elif cellCoordinates[0] == len(maze) - 1:
        res.append(None)
    if cellCoordinates[1] > 0:
        res.append((cellCoordinates[0], cellCoordinates[1] - 1))
    elif cellCoordinates[1] == 0:
        res.append(None)
    if cellCoordinates[1] < len(maze[0]) - 1:
        res.append((cellCoordinates[0], cellCoordinates[1] + 1))
    elif cellCoordinates[1] == len(maze[0]) - 1:
        res.append(None)
    return res

def checkPrefabs(maze, intPrefabs, cellCoordinates):
    neighborsList = checkNeighbors(maze, cellCoordinates)
    if intPrefabs == 3:
        if neighborsList[3] == None or maze[neighborsList[3][0]][neighborsList[3][1]] == '#':
            return '╣'
        elif neighborsList[2] == None or maze[neighborsList[2][0]][neighborsList[2][1]] == '#':
            return '╟'
        elif neighborsList[0] == None or maze[neighborsList[0][0]][neighborsList[0][1]] == '#':
            return '╦'
        else:
            return '╩'
    elif intPrefabs == 2:
        if (neighborsList[2] == None or maze[neighborsList[2][0]][neighborsList[2][1]] == '#') and (neighborsList[3] == None or maze[neighborsList[3][0]][neighborsList[3][1]] == '#'):
            return '║'
        elif (neighborsList[1] == None or maze[neighborsList[1][0]][neighborsList[1][1]] == '#') and (neighborsList[0] == None or maze[neighborsList[0][0]][neighborsList[0][1]] == '#'):
            return '═'
        elif (neighborsList[0] == None or maze[neighborsList[0][0]][neighborsList[0][1]] == '#') and (neighborsList[3] == None or maze[neighborsList[3][0]][neighborsList[3][1]] == '#'):
            return '╗'
        elif (neighborsList[0] == None or maze[neighborsList[0][0]][neighborsList[0][1]] == '#') and (neighborsList[2] == None or maze[neighborsList[2][0]][neighborsList[2][1]] == '#'):
            return '╔'
        elif (neighborsList[1] == None or maze[neighborsList[1][0]][neighborsList[1][1]] == '#') and (neighborsList[2] == None or maze[neighborsList[2][0]][neighborsList[2][1]] == '#'):
            return '╚'
        elif (neighborsList[1] == None or maze[neighborsList[1][0]][neighborsList[1][1]] == '#') and (neighborsList[3] == None or maze[neighborsList[3][0]][neighborsList[3][1]] == '#'):
            return '╝'
    elif intPrefabs == 1:
        if neighborsList[3] != None and maze[neighborsList[3][0]][neighborsList[3][1]] == '1':
            return '►'
        if neighborsList[2] != None and maze[neighborsList[2][0]][neighborsList[2][1]] == '1':
            return '◄'
        if neighborsList[0] != None and maze[neighborsList[0][0]][neighborsList[0][1]] == '1':
            return '▲'
        if neighborsList[1] != None and maze[neighborsList[1][0]][neighborsList[1][1]] == '1':
            return '▼'
    elif intPrefabs == 4:
        return '╬'

def typeOfPrefabs(maze, cellCoordinates):
    if maze[cellCoordinates[0]][cellCoordinates[1]] == '#':
        return '#'
    neighbors = checkNeighbors(maze, cellCoordinates)
    totalNeighbors = 0
    for neighbor in neighbors:
        if neighbor != None:
            if maze[neighbor[0]][neighbor[1]] == '1':
                totalNeighbors += 1
    return checkPrefabs(maze, totalNeighbors, cellCoordinates)
    
def generateBasicMaze(size):
    return [['#' for _ in range(size)] for _ in range(size)]

def pathGenerator(maze, pathLength):
    path = []
    startCell = [random.randint(0, len(maze) - 1), random.randint(0, len(maze[0]) - 1)]
    path.append(startCell)
    while len(path) <= pathLength:
        neighbors = checkNeighbors(maze, path[-1])
        neighbor = neighbors[random.randint(0, 1000) % len(neighbors)]
        if neighbor != None and maze[neighbor[0]][neighbor[1]] not in path:
            path.append(neighbor)
    return path

maze = generateBasicMaze(10)
path = pathGenerator(maze, 40)

for cell in path:
    maze[cell[0]][cell[1]] = '1'

res = []
for row in range(len(maze[0])):
    submaze = []
    for col in range(len(maze[1])):
        submaze.append(typeOfPrefabs(maze, [row, col]))
    res.append(submaze)

for i in res:
    i = map(lambda x: x.replace('#', ' '), i)
    print(''.join(i))