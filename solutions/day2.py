import sys

def parseInput():
    l1 = []
    try: 
        with open("inputs/day2.txt") as file:
            lines = file.readlines()
    except Exception as e:
        print(f"no input???: {e}")
        return [], []

    for line in lines:
        l1.append([int(x) for x in line.strip().split()])

    return l1

def checker(m):
    safe = True
    dir = None
    lastDiff = 0
    for n in range(len(m) - 1):
        diff =  m[n] - m[n+1]
        
        if (diff > 3) or (diff < -3) or (diff == 0) or ((lastDiff > 0) and (diff < 0)) or ((lastDiff < 0) and (diff > 0)):
            safe = False
            break
        lastDiff = diff
    return safe

def part1(l):
    total = 0
    for m in l:
        if checker(m): total += 1
    print("Day 2 - Part 1: ", total)

def part2(l):
    total = 0
    for m in l:
        for n in range(len(m)):
            if checker(m[:n]+m[n+1:]): 
                total += 1
                break

    print("Day 2 - Part 2: ", total)

def main():
    l = parseInput()
    if sys.argv[1] == "1":
        part1(l)
    elif sys.argv[1] == "2":
        part2(l)

if __name__ == "__main__":
    main()