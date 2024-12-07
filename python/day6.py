from pprint import pprint

def walk(themap, row, col):
    dcol = 0
    drow = -1
    dir = 0
    seen = {}    
    while True:        
        if (row,col,dir) in seen:
            return (set(), True)
        seen[(row,col,dir)] = True
        (nextr,nextc) = (row+drow, col+dcol)
        if not ( nextr in range(len(themap)) and nextc in range(len(themap[0])) ):
            break
        if themap[nextr][nextc] == "#":
            dir = (dir + 1) % 4
            match dir:
                case 0 : (dcol,drow) = (0,-1)
                case 1 : (dcol,drow) = (1,0)
                case 2 : (dcol,drow) = (0,1)
                case 3 : (dcol,drow) = (-1,0)
        else:            
            col = nextc
            row = nextr

    visited = [(r,c) for (r,c,d) in seen]
    return (set(visited), False)

def day6(input):
    themap = []
    col = -1
    for (i, irow) in enumerate(input):
        themap.append(list(irow))
        if '^' in irow:
            row = i
            col = irow.index('^')            
    themap[row][col] = '.'

    loops = 0
        
    (result1, _) = walk(themap, row, col)
    for (r,c) in result1:        
        themap[r][c] = '#'
        (_, looped) = walk(themap, row, col)
        themap[r][c] = '.'
        if looped:
            loops += 1
    print(len(result1),loops)


#41, 6
input = open("src/bin/inputs/day6.test1.txt", "r").readlines()
day6(input)

#4988, 1697
input = open("src/bin/inputs/day6.txt", "r").readlines()
day6(input)