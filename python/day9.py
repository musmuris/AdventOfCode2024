from pprint import pprint
from itertools import combinations


def compact_all(disk):
    write = 0
    while True:
        # Skip blanks at the end
        while disk[-1] == '.':
            disk.pop()

        if write >= len(disk):
            break
        if disk[write] != '.':
            write += 1
            continue
        # need to move a block from right to here
        disk[write] = disk.pop()

def compact_nofrag(disk):
    read = len(disk) - 1
    seen={}
    while True:
        if len(disk) < 100:
            print(''.join([str(x) for x in disk]))
        # Skip blanks at the end
        while disk[read] == '.':
            read -= 1
            if read < 0:
                return

        # Find next file
        fileEnd = read
        fileId = disk[read]

        while disk[read] == fileId:
            read -= 1
        if fileId in seen:
            continue

        fileLen = fileEnd - read
        seen[fileId] = True

        print(f"fileid {fileId}  len {fileLen}")

        freeSize = 0
        freeStart = 0
        for i in range(read + 1):
            if disk[i] == '.':
                freeSize += 1
                if freeSize >= fileLen:
                    freeStart += 1
                    break
            else:
                freeStart = i
                freeSize = 0

        if freeSize >= fileLen:
            for i in reversed(range(freeStart, freeStart+freeSize)):
                disk[i] = disk[fileEnd]
                disk[fileEnd] = '.'
                fileEnd -= 1

def day9(input):
    disk = []
    file = True
    fileId = 0
    for c in input:
        l = int(c)
        if file:
            disk += [fileId] * l
            fileId += 1
        else:
            disk += ['.'] * l
        file = not file

#    print(disk)
    # Always backup first
    backup = [x for x in disk]

    compact_all(disk)

    # checksum
    acc = 0
    for i in range(len(disk)):
        if disk[i] == '.':
            continue
        acc += disk[i] * i

    disk = backup
    compact_nofrag(disk)

    # checksum
    acc2 = 0
    for i in range(len(disk)):
        if disk[i] == '.':
            continue
        acc2 += disk[i] * i

    return(acc, acc2)

#(1928, 2858)
input = open("src/bin/inputs/day9.test1.txt", "r").read()
pprint(day9(input.strip()))

#(1928, 2826)
input = open("src/bin/inputs/day9.test2.txt", "r").read()
pprint(day9(input.strip()))

#(6461289671426, 6488291456470)
input = open("src/bin/inputs/day9.txt", "r").read()
pprint(day9(input.strip()))
