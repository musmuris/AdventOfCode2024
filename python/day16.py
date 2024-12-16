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
    heapq.heappush(priQ, (0 , start, (0,1)))
    costs = {}
    routes = {}
    costs[start] = 0
    routes[start] = set()
    routes[start].add(start)

    while len(priQ) > 0:
        current = heapq.heappop(priQ)
        old_cost, (r,c),old_dcost = current

        for dr,dc in paths:
            nr,nc = r+dr, c+dc
            if maze[nr][nc] == '#':
                continue
            dcost = 1
            if (dr,dc) != old_dcost:
                dcost += 1000
            loc = (nr,nc)
            new_cost = costs[(r,c)] + dcost
            if loc not in costs or new_cost <= costs[loc]:
                update_routes = loc not in costs or new_cost == costs[loc]
                costs[loc] = new_cost
                if update_routes:
                    if loc not in routes:
                        routes[loc] = set(routes[(r,c)])
                    else:
                        routes[loc].update(routes[(r,c)])
                else:
                    routes[loc] = set(routes[(r,c)])
                routes[loc].add(loc)
                heapq.heappush(priQ, (new_cost, loc, (dr,dc)))
    pprint(len(routes[end]))
    print_maze(maze, routes[end])
    pprint(routes[end])
    return costs[end]

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


# input = open("src/bin/inputs/day16.test1.txt", "r").read().splitlines()
# pprint(day16(input))

input = open("src/bin/inputs/day16.test3.txt", "r").read().splitlines()
pprint(day16(input))



# input = open("src/bin/inputs/day16.test2.txt", "r").read().splitlines()
# pprint(day16(input))


# input = open("src/bin/inputs/day16.txt", "r").read().splitlines()
# pprint(day16(input))
