from pprint import pprint
from itertools import combinations

class Finder:

    def find_pair_nodes(self, r, c, dr, dc):
        d = 0
        while True:
            nr = r+(dr*d)
            nc = c+(dc*d)
            if not(nr in range(self.height) and nc in range(self.width)):
                break
            self.harmonic_nodes.add((nr,nc))
            if d == 1:
                self.nodes.add((nr,nc))
            d += 1

    def find_nodes(self):    
        for atype in self.ants:        
            for pair in set(combinations(self.ants[atype], 2)):                
                ((r1, c1),(r2,c2)) = pair
                dr = r1-r2
                dc = c1-c2

                self.find_pair_nodes(r1, c1, dr, dc)
                self.find_pair_nodes(r2, c2, -dr, -dc)
            
    def find_ants(self):
        ants = {}        
        for r,line in enumerate(input):        
            for c,a in enumerate(line):
                if a != '.':
                    if not a in ants:
                        ants[a]=[]
                    ants[a].append((r,c))
        self.ants = ants
        
        
    def run(self, input):        
        self.input = input        
        self.height = len(input)
        self.width = len(input[0])
        self.nodes = set()
        self.harmonic_nodes = set()
        
        self.find_ants()
        self.find_nodes()

        return(len(self.nodes),len(self.harmonic_nodes))

def day8(input):
    f = Finder()
    return f.run(input)

#14 34
input = open("src/bin/inputs/day8.test1.txt", "r").read().splitlines()
pprint(day8(input))

#276 991
input = open("src/bin/inputs/day8.txt", "r").read().splitlines()
pprint(day8(input))