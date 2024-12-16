from pprint import pprint

def day0(input):
    acc1 = len(input)
    acc2 = len(input)
    return acc1,acc2

input = open("src/bin/inputs/day0.test1.txt", "r").read()
pprint(day0(input.strip()))


input = open("src/bin/inputs/day0.txt", "r").read()
pprint(day0(input.strip()))
