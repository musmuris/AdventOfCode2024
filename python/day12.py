from pprint import pprint
from collections import defaultdict

paths = [ (0,1), (0,-1), (1,0), (-1,0)]

def walk_plot(map, pos, seen):

    x,y = pos
    seen.add((x,y))
    adj = 0
    plot = set([(x,y)])
    perim = 0
    for dx,dy in paths:
        nx,ny =  (x+dx, y+dy)
        if nx in range(len(map)) and ny in range(len(map[0])):
            if map[ny][nx] == map[y][x]:
                adj += 1
                if not (nx,ny) in seen:
                    (a,b) = walk_plot(map, (nx,ny), seen)
                    plot.update(a)
                    perim += b

    return (plot, 4-adj + perim)

def day12(input):
    map = [[p for p in line] for line in input]
    seen = set()
    acc = 0
    for y in range(len(map)):
        for x in range(len(map[0])):
            if not (x,y) in seen:
                (plot, perim) = walk_plot(map, (x,y), seen)
                print(f"{map[y][x]} {(plot, perim)}")
                acc += len(plot) * perim
    print(acc)

input = open("src/bin/inputs/day12.test1.txt", "r").read().splitlines()
pprint(day12(input))


input = open("src/bin/inputs/day12.txt", "r").read().splitlines()
pprint(day12(input))
