import math

# As my solution was quite slooooow I went looking at others
# One used recursion so I went to replicate that and it is a 
# lot faster (hence me going back to try improve mine - see comment in there)

def runopsrec(nums, inx, target, acc, do2):
    if acc > target:
        return False
    if inx == len(nums):
        return acc == target
    if runopsrec(nums, inx + 1, target, acc * nums[inx], do2):
        return True
    if runopsrec(nums, inx + 1, target, acc + nums[inx], do2):
        return True    
    if do2:
        acc = int(str(acc) + str(nums[inx]))
        if runopsrec(nums, inx + 1, target, acc, do2):
            return True
    return False

def day7(input):
    result1 = 0
    result2 = 0
    lc = 0
    for line in input:
        print(f"{lc}/{len(input)}")
        lc += 1
        l = line.split()
        target = int(l[0][:-1])
        nums = [int(i) for i in l[1:]]

        if runopsrec(nums, 1, target, nums[0], False):
            result1 += target
            
        if runopsrec(nums, 1, target, nums[0], True):        
            result2 += target

    print(f"{result1} {result2}")

#3749 11387
input = open("src/bin/inputs/day7.test1.txt", "r").readlines()
day7(input)

#12940396350192 106016735664498
input = open("src/bin/inputs/day7.txt", "r").readlines()
day7(input)