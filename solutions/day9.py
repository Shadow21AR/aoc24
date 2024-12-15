import sys

def moveFiles(disk):
    left = 0
    right = len(disk)-1
    while left < right:
        while left < len(disk) and disk[left] != ".":
            left += 1
        while right > left and disk[right] == ".":
            right -= 1
        if left < right:
            disk[left], disk[right] = disk[right], "."
            left += 1
            right -= 1
    return disk

def findSizes(disk):
    sizes = {}
    for n in disk:
        if n == ".":
            continue
        if int(n) in sizes:
            sizes[int(n)] += 1
        else:
            sizes[int(n)] = 1
    return sizes

def findDots(disk, seqLen):
    for i in range(len(disk) - seqLen +1):
        if ''.join(disk[i:i+seqLen]) == "." * seqLen:
            return i
    return -1

def moveWholeFiles(disk):
    sizes = findSizes(disk)
    id = max(sizes)
    while id >= 0:
        left = findDots(disk, sizes[id])
        idIndex = disk.index(str(id))
        if left == -1:
            id -= 1
            continue
        if left > idIndex:
            id -= 1
            continue
        if ''.join(disk[left:left+sizes[id]]) == "." * sizes[id]:
        # if all(disk[i] == "." for i in range(left, left + sizes[id])):
            for i in range(left, left+sizes[id]):
                disk[i] = str(id)
            for i in range(idIndex, idIndex + sizes[id]):
                disk[i] = "."
        id -= 1
    return disk

def total(disk):
    total = 0
    for i, char in enumerate(disk):
        if char == ".":
            continue
        total += i * int(char)
    return total


def part1(disk):
    print("Day 9 - Part 1 :", total(moveFiles(disk)))

def part2(disk):
    print("Day 9 - Part 2 :", total(moveWholeFiles(disk)))

def main():
    data = open("inputs/day9.txt").read().strip()
    # data = "2333133121414131402".strip()
    id = 0
    disk = []
    for i, num in enumerate(data):
        if i % 2 == 0:
            disk.extend([str(id)] * int(num))
            id += 1
        else:
            disk.extend(["."] * int(num))

    if sys.argv[1] == "1":
        part1(disk)
    elif sys.argv[1] == "2":
        part2(disk)

if __name__ == "__main__":
    main()