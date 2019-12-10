from math import gcd, sqrt, asin, degrees
import collections

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

# possible discrete directions in a 40x40 grid
def calcAngle(x,y):
    # normalize vector
    length = sqrt((x * x) + (y * y))
    if length > 0:
        x /= length
        y /= length
    # top right: 
    if x <= 0 and y >= 0:
        return degrees(asin(y))
    # bottom right:
    elif x > 0 and y >= 0:
        return 90+degrees(asin(x))
    # bottom left
    if x > 0 and y < 0:
        return 180+degrees(asin(abs(y)))
    # top left 
    if x <= 0 and y < 0:
        return 270+degrees(asin(abs(x)))

#def calcDirections():
dirs = {}
dir_coords = []
for i in range(-40, 41):
    for j in range(-40, 41):
        dir_x = i
        dir_y = j
        if gcd(i, j) != 0:
            dir_x = i / gcd(i,j)
            dir_y = j / gcd(i,j)
        dir_coords.append((int(dir_x), int(dir_y)))
for coords in set(dir_coords):
    dirs[calcAngle(coords[0],coords[1])] = coords
sorted_dirs = collections.OrderedDict(sorted(dirs.items()))        
#return sorted_dirs

def hitAsteroid(x, y, x_step, y_step):
    if x_step == 0 and y_step == 0:
        return 0
    x += x_step
    y += y_step   
    while (x < width and x >= 0) and (y < height and y >= 0):
       if asteroidField[x][y] == "#":
           asteroidField[x][y] = "."
           print("hit #{}: x={} y={}".format(hitCount, y, x))
           return 1
       x += x_step
       y += y_step
    return 0

hitCount = 0
print(sorted_dirs)
while hitCount < 200:
    for key,value in sorted_dirs.items():
        hit = hitAsteroid(20, 31, value[0], value[1])
        if hit:
            hitCount += 1
        if hitCount > 200:
            break
