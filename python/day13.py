from pprint import pprint
import re
import heapq
import math


def dist_to_target(pos,target):
    x,y = pos
    tx,ty = target
    return math.sqrt((tx-x)**2 + (ty-y)**2)

def a_star(end, ba, bb):
    pri_q = []
    heapq.heappush(pri_q, (0,(0,0,0,0,0)))
    gx,gy = end
    gx += 10000000000000
    gy += 10000000000000
    costs = {}
    done = set()

    s = 0
    while len(pri_q) > 0:        
        pri,(cost,x,y,pa,pb) = heapq.heappop(pri_q)    
        if s % 1000 == 0:
            print(f"{pri} {x} {y}")
        s+=1
        for path in [(3,ba,1,0), (1,bb,0,1)]:            
            dc,(dx,dy),dpa,dpb = path
            nx,ny = x + dx, y + dy
            npa,npb = pa + dpa, pb + dpb
            nc = cost + dc            
            if nx <= gx and ny <= gy and (npa,npb) not in done and dpa <= 100 and dpb <= 100: 
                if (nx,ny) not in costs or nc < costs[(nx,ny)]:
                    costs[(nx,ny)] = nc
                    done.add((npa,npb))
                    h = dist_to_target((nx,ny),(gx,gy))
                    heapq.heappush(pri_q, (nc+h, (nc,nx,ny,npa,npb)))
        pri_q = pri_q[:100]
    
    if end in costs:
        return (True,costs[end])
    else:
        return (False,0)
    
def day13(input):
    acc1 = 0
    acc2 = len(input)

    reg = re.compile(r"Button A: X\+(\d*), Y\+(\d*)\s*Button B: X\+(\d*), Y\+(\d*)\s*Prize: X=(\d*), Y=(\d*)")
    for m in reg.finditer(input):
        if len(m.groups()) != 6:
            raise ValueError("oh dear")
        ba = (int(m.group(1)), int(m.group(2)))
        bb = (int(m.group(3)), int(m.group(4)))
        p = (int(m.group(5)), int(m.group(6)))
        
        ok,cost = a_star(p, ba, bb)
        print(ok,cost)
        if ok:
            acc1 += cost

    return acc1,acc2

input = open("src/bin/inputs/day13.test1.txt", "r").read()
pprint(day13(input.strip()))

# input = open("src/bin/inputs/day13.test2.txt", "r").read()
# pprint(day13(input.strip()))


# input = open("src/bin/inputs/day13.txt", "r").read()
# pprint(day13(input.strip()))
