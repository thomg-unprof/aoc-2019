from math import gcd

with open("/workspace/aoc-2019/day10/python/thomg/asteroids") as file:
    asteroidLines = file.readlines()

width = len(asteroidLines[0])-1
height = len(asteroidLines)
asteroidField = []
for i in range(width):
    asteroidField.append([])
j = 0
for line in asteroidLines:
    for i in range(width):
        asteroidField[j].append(line[i])
    j += 1
for y in range(height):
    print(asteroidField[:][y])

def calcDirections(x, y):
    # dont do -1 here because that will be taken care of by python range
    xToRight = width - x
    yToBottom = height - y

    dirList = []
    for i in range(-x, xToRight):
        for j in range(-y, yToBottom):
            dir_x = i
            dir_y = j
            if gcd(i,j) != 0:
                dir_x /= gcd(i, j)
                dir_y /= gcd(i, j)
            dirList.append((int(dir_x), int(dir_y)))
    return dirList

def hitAsteroid(x, y, x_step, y_step):
    if x_step == 0 and y_step == 0:
        return 0
    x += x_step
    y += y_step   
    while (x < width and x >= 0) and (y < height and y >= 0):
       if asteroidField[x][y] == "#":
           return (x,y)
       x += x_step
       y += y_step
    return None

maxHits = 0
bestCoords = (0,0)
for x in range(width):
    for y in range(height):
        if asteroidField[x][y] != "#":
            continue
        hitCoords = []
        dirList = calcDirections(x, y)
        if x == 0 and y == 6:
            print("debug!")
        for dir in set(dirList):
            #hitCount += hitAsteroid(x, y, item[0], item[1])
            hit = hitAsteroid(x, y, dir[0], dir[1])
            if hit:
                hitCoords.append(hit)
        hitCount = len(set(hitCoords))
        if hitCount > maxHits:
            maxHits = hitCount
            bestCoords = (x,y)
        
print(maxHits, bestCoords)