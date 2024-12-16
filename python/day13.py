from pprint import pprint
import re
import heapq
import math


def solve(end, ba, bb, extra):
    r1,r2 = end
    a1,a2 = ba
    b1,b2 = bb

    r1 += extra
    r2 += extra

    c1 = r1/a1 * a2
    c2 = ((-b1)/a1) * a2
    bcount = (r2-c1) / (c2 + b2)
    acount = (r1 - (b1 * bcount))/a1

    bcount = round(bcount)
    acount = round(acount)
    check1 = (a1 * acount) + (b1 * bcount)
    check2 = (a2 * acount) + (b2 * bcount)
    if (check1, check2) != (r1,r2):
        return 0
    
    return acount * 3 + bcount

    
def day13(input):
    acc1 = 0
    acc2 = 0

    reg = re.compile(r"Button A: X\+(\d*), Y\+(\d*)\s*Button B: X\+(\d*), Y\+(\d*)\s*Prize: X=(\d*), Y=(\d*)")
    for m in reg.finditer(input):
        if len(m.groups()) != 6:
            raise ValueError("oh dear")
        ba = (int(m.group(1)), int(m.group(2)))
        bb = (int(m.group(3)), int(m.group(4)))
        p = (int(m.group(5)), int(m.group(6)))
        
        acc1 += solve(p, ba, bb, 0)
        acc2 += solve(p, ba, bb, 10000000000000)

    return acc1,acc2

input = open("src/bin/inputs/day13.test1.txt", "r").read()
pprint(day13(input.strip()))


input = open("src/bin/inputs/day13.txt", "r").read()
pprint(day13(input.strip()))
