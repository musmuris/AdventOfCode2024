from pprint import pprint
import re
import time

class Bot:
    def __init__(self, x,y,vx,vy):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
    
    def __repr__(self) -> str:
        return f"({self.x}, {self.y})"
             
        
def check_map(lines, w, h):
    for y in range(2,h-2):
            for x in range(2,w-2):
                c = 0
                for dx,dy in [(0,0),(0,1),(0,-1),(1,0),(-1,0),(0,2),(0,-2),(2,0),(-2,0)]:
                    if lines[y+dy][x+dx] == '#':
                         c += 1
                if c == 9:
                    print("\033[H\033[J", end="")
                    for l in lines:
                        print("".join(l))
                                        
                    return True

    return False
            

def day14(input, size):
    w,h = size
    reg = re.compile(r"p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)")
    bots = []
    for l in input:
        m = reg.match(l)
        bots.append(Bot(int(m.group(1)),
                        int(m.group(2)),
                        int(m.group(3)),
                        int(m.group(4))))
            
    for s in range(10000):
        lines = [[' ' for x in range(w)] for y in range(h)]
        for bot in bots:
            bot.x = (bot.x+bot.vx) % w
            bot.y = (bot.y+bot.vy) % h
            lines[bot.y][bot.x] = '#'
        if check_map(lines, w, h):
            print(s)
            time.sleep(1)
        if s % 100 == 0:
            print(s)
    # quads=[ [],[],[],[]]
    # for bot in bots:
    #     quad = 0
    #     if bot.x == w // 2 or bot.y == h // 2:
    #         continue
    #     if bot.x > w // 2:
    #         quad += 1 
    #     if bot.y > h // 2:
    #         quad += 2 
    #     quads[quad].append(bot)
    
    # acc1 = 1
    # for q in quads:
    #     acc1 *= len(q)

    return (acc1,0)

# input = open("src/bin/inputs/day14.test1.txt", "r").read().splitlines()
# pprint(day14(input,(11,7)))


input = open("src/bin/inputs/day14.txt", "r").read().splitlines()
pprint(day14(input,(101,103)))
