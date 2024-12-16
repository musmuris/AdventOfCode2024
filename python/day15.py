from pprint import pprint
import os
import time


dirs = { 
    '^' : (-1,0),
    'v' : (1,0),
    '<' : (0,-1),
    '>' : (0,1)
}


def print_warehouse(w, bot):
    print("\033[H\033[J", end="")
    br,bc = bot
    w[br][bc] = '@'
    for l in w:
        print("".join(l))
    w[br][bc] = '.'    

def move_box(warehouse, box, move):
    br,bc = box    
    dr,dc = move
    nr,nc = br+dr,bc+dc
    if warehouse[nr][nc] == '.':
        warehouse[nr][nc] = 'O'
        warehouse[br][bc] = '.'
        return True
    if warehouse[nr][nc] == '#':
        return False
    if warehouse[nr][nc] == 'O' and move_box(warehouse, (nr, nc), move):
        warehouse[nr][nc] = 'O'
        warehouse[br][bc] = '.'
        return True
    return False

def run(warehouse, moves, bot):
    br,bc = bot
    for c,m in enumerate(moves):
        #print_warehouse(warehouse, (br,bc))
        #print(f"{c} {m}")
        #time.sleep(0.01)
        dr,dc = m
        nr,nc = br+dr,bc+dc
        if warehouse[nr][nc] == '.':
            br,bc = nr,nc
            continue
        if warehouse[nr][nc] == '#':
            continue
        if move_box(warehouse, (nr,nc), m):
            br,bc = nr,nc

def gps(warehouse):
    acc = 0
    for r in range(len(warehouse)):
        for c in range(len(warehouse[r])):
            if warehouse[r][c] == 'O':
                acc += (100*r) + c
    return acc


def day15(input):
    warehouse = []
    for r,l in enumerate(input):
        if len(l) == 0:
            break
        line = []
        for c,m in enumerate(l):
            if m == '@':
                line.append('.')
                bot = (r,c)
            else:
                line.append(m)
        warehouse.append(line)
    
    moves = []
    for l in input[r:]:
        moves += [dirs[c] for c in l]
    run(warehouse, moves, bot)
    print(gps(warehouse))


input = open("src/bin/inputs/day15.test1.txt", "r").read().splitlines()
pprint(day15(input))

input = open("src/bin/inputs/day15.txt", "r").read().splitlines()
pprint(day15(input))
