import sys

def parseInput():
    l1 = []
    l2 = []
    try: 
        with open("inputs/day1.txt") as file:
            lines = file.readlines()
    except Exception as e:
        print(f"no input???: {e}")
        return [], []

    for line in lines:
        n = line.strip().split()
        l1.append(int(n[0]))
        l2.append(int(n[1]))

    l1.sort()
    l2.sort()
    return l1, l2

def part1(l1, l2):
    sum = 0
    for i in range(len(l1)):
        sum += abs(l1[i]-l2[i])
    print(f"Day 1 - Part 1: {sum}")

def part2(l1, l2):
    sum = 0
    for i in l1:
        sim = 0
        for j in l2:
            if j > i: break
            if j == i: sim += 1
        sum += i * sim

    print(f"Day 1 - Part 2: {sum}")


def main():
    l1, l2 = parseInput()
    if sys.argv[1] == "1":
        part1(l1, l2)
    elif sys.argv[1] == "2":
        part2(l1,l2)

if __name__ == "__main__":
    main()