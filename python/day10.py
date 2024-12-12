from pprint import pprint
from itertools import combinations
from collections import deque

class Walker:

    paths = [ (0,1), (0,-1), (1,0), (-1,0)]
    
    def walk(self, node):
        #pprint(f"node {node}")
        
        if node in self.maptotarget:
            return self.maptotarget[node]
        
        x,y = node
        if self.map[x][y] == 9:            
            e = set([node])            
            return e
        
        localpaths = set()
        for dx,dy in self.paths:
            nx,ny =  (x+dx, y+dy)
            if nx in range(self.w) and ny in range(self.h):
                if self.map[nx][ny] == (self.map[x][y]+1):
                    r = self.walk((nx,ny))                
                    localpaths.update(r)
        self.maptotarget[node] = localpaths
        return self.maptotarget[node]

    def run(self, input):
        self.h = len(input)  
        self.w = len(input[0]) 
        self.map = [[-1]*self.h for l in range(self.w)]
        self.starts = set()
        self.targets = set()
        for y in range(self.w):
            for x in range(self.h):
                self.map[x][y] = int(input[y][x])
                if self.map[x][y] == 0:
                    self.starts.add((x,y))
                elif self.map[x][y] == 9:
                    self.targets.add((x,y))    

        self.maptotarget = {}
        sum = 0
        for start in self.starts:            
            sum += len(self.walk(start))

        print(sum)

def day10(input):
    w = Walker()
    w.run(input)

input = open("src/bin/inputs/day10.test1.txt", "r").read().splitlines()
pprint(day10(input))

# input = open("src/bin/inputs/day10.test2.txt", "r").read().splitlines()
# pprint(day10(input))

input = open("src/bin/inputs/day10.txt", "r").read().splitlines()
pprint(day10(input))