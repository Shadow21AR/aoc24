import sys
from itertools import product


def parse(data):
    out = {}
    for line in data.split("\n"):
        nums = line.split(":")
        out[int(nums[0].strip())] = [int(x) for x in nums[1].strip().split(" ")]
    return out

def solve(data, operators):
    nice = set()
    for k,v in data.items():
        combination = product(operators, repeat=len(v)-1)

        for ops in combination:
            total = v[0]
            for i, op in enumerate(ops):
                if op == "+":
                    total += v[i+1]
                elif op == "*":
                    total *= v[i+1]
                elif op == "||":
                    total = int(str(total) + str(v[i+1]))

            if total == k:
                nice.add(k)
                break
    return sum(nice)

def part1(data):
    print("Day 7 - Part 1 : ", solve(data, ["+", "*"]))

def part2(data):
    print("Day 7 - Part 2 : ", solve(data, ["+", "*", "||"]))

def main():
    file = open("inputs/day7.txt").read().strip()
    data = parse(file)
    if sys.argv[1] == "1":
        part1(data)
    elif sys.argv[1] == "2":
        part2(data)

if __name__ == "__main__":
    main()