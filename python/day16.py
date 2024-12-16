from pprint import pprint
from collections import defaultdict
import heapq

paths = [(0,1), (0,-1), (1,0), (-1,0)]

def print_maze(maze, routes):
    for r in range(len(maze)):
        for c in range(len(maze[0])):
            if (r,c) in routes:
                print("0", end="")
            else:
                print(maze[r][c], end="")
        print()

def path_find(maze, start, end):
    priQ = []
    initial_route = set()
    initial_route.add(start)
    heapq.heappush(priQ, (0 , start, (0,1), initial_route ))
    costs = {}
    routes = {}
    costs[start] = 0
    routes = []
    min_cost = 1000000000

    while len(priQ) > 0:
        current = heapq.heappop(priQ)
        old_cost, (r,c),old_dcost, route = current

        for dr,dc in paths:
            nr,nc = r+dr, c+dc
            if maze[nr][nc] == '#':
                continue
            dcost = 1
            if (dr,dc) != old_dcost:
                dcost += 1000
            loc = (nr,nc)
            if loc in route: # don't backtrack
                continue
            new_route = set(route)
            new_route.add(loc)
            new_cost = old_cost + dcost
            if loc == end:
                if new_cost < min_cost:
                    min_cost = new_cost
                routes.append((new_cost, new_route))
                break # found end
            if new_cost > min_cost:
                continue # already found better path

            if (loc,dr,dc) not in costs or new_cost <= costs[(loc,dr,dc)]:
                costs[(loc,dr,dc)] = new_cost
                heapq.heappush(priQ, (new_cost, loc, (dr,dc), new_route))

    points = set()
    for r in routes:
        if r[0] == min_cost:
            points.update(r[1])
    print_maze(maze, points)
    return (min_cost, len(points))

def day16(input):
    maze = [[p for p in line] for line in input]
    for r in range(len(maze)):
        for c in range(len(maze[0])):
            if maze[r][c] == 'S':
                start = (r,c)
                maze[r][c] = '.'
            elif maze[r][c] == 'E':
                end = (r,c)
                maze[r][c] = '.'#
    acc1 = path_find(maze, start, end)
    return acc1


input = open("src/bin/inputs/day16.test1.txt", "r").read().splitlines()
pprint(day16(input))


input = open("src/bin/inputs/day16.test2.txt", "r").read().splitlines()
pprint(day16(input))

# input = open("src/bin/inputs/day16.test3.txt", "r").read().splitlines()
# pprint(day16(input))

input = open("src/bin/inputs/day16.txt", "r").read().splitlines()
pprint(day16(input))
