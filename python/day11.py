from pprint import pprint
from collections import defaultdict


def count_stones(stones):
    return sum([c for _,c in stones.items()])

def day11(input):

    stones = defaultdict(lambda:0)
    for s in [int(s) for s in input.split()]:
        stones[s] += 1

    print(stones)

    for i in range(75):
        newstones = defaultdict(lambda:0)
        for s,c in stones.items():
            if s == 0:
                newstones[1] += c
            else:
                x = str(s)
                if len(x) % 2 == 0:
                    newstones[int(x[:len(x)//2])] += c
                    newstones[int(x[len(x)//2:])] += c
                else:
                    newstones[s * 2024] += c
        stones = newstones
        if i == 24:
            acc1 = count_stones(stones)
    acc2 = count_stones(stones)
    return acc1,acc2

input = open("src/bin/inputs/day11.test1.txt", "r").read()
pprint(day11(input.strip()))


input = open("src/bin/inputs/day11.txt", "r").read()
pprint(day11(input.strip()))
