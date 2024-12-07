from pprint import pprint

def walk(themap, row, col):
    dcol = 0
    drow = -1
    dir = 0
    visted = 1
    seen = {}
    themap[row][col] = 'X'
    while True:
        #pprint(walked)
        if (dir,row,col) in seen:
            return (visted, True)
        seen[(dir,row,col)] = True
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
            if themap[nextr][nextc] != "X":
                visted += 1
                themap[nextr][nextc] = "X"
            col = nextc
            row = nextr

    return (visted, False)

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
    mapcopy = [row[:] for row in themap]
    (result1, _) = walk(mapcopy, row, col)
    for orow in range(len(themap)):
        for ocol in range(len(themap[0])):
            if themap[orow][ocol] == ".":
                mapcopy = [l[:] for l in themap]
                mapcopy[orow][ocol] = "#"
                #pprint(mapcopy)
                (_, looped) = walk(mapcopy, row, col)
                if looped:
                    loops += 1
    print(result1,loops)


#41, 6
input = open("src/bin/inputs/day6.test1.txt", "r").readlines()
day6(input)

#4988, 1697
input = open("src/bin/inputs/day6.txt", "r").readlines()
day6(input)