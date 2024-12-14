# Here I started by making a binary number as the two "ops" 0 => + and 1 => *
# Then the part2 cureball was adding another op of || so I had to find a way
# to make tenary numbers - but this was slow
# It's also somewhat horrible and I wish I'd spent longer thinking about it first!

def runops(nums, ops, target):
    acc = nums[0]
    for i,op in enumerate(ops):
        if op == '2':
            acc = int(str(acc) + str(nums[i+1]))
        elif op == '1':
            acc *= nums[i+1]
        elif op == '0':
            acc += nums[i+1]
        if acc > target:
            return False
    return acc == target

# Originally this wasn't memoized and it turns
# out this is slow. Memoizing improved it a bit!
# (see also day7_faster)
memoize = {}
def ternary(num, l):
    n = num
    if (num,l) in memoize:
        return memoize[(num,l)]
    digits = [0]*l
    for i in range(l):
        (num,r) = divmod(num,3)
        digits[i] = r
    res = ''.join(str(x) for x in reversed(digits))
    memoize[(n,l)] = res
    return res

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

        oppow = 2 ** (len(nums) - 1)
        fo = f"0{len(nums) - 1}b"
        for i in range(oppow):
            ops = format(i, fo)
            if runops(nums,ops,target):
                result1 += target
                break

        oppow = 3 ** (len(nums) - 1)
        for i in range(oppow):
            ops = ternary(i, len(nums) - 1)
            if runops(nums,ops,target):
                result2 += target
                break

    print(f"{result1} {result2}")

#3749 11387
input = open("src/bin/inputs/day7.test1.txt", "r").readlines()
day7(input)

#12940396350192 106016735664498
input = open("src/bin/inputs/day7.txt", "r").readlines()
day7(input)