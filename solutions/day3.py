import sys, re


def mul(a,b):
    return a*b

def part1(file):
    pattern = r"mul\([0-9]{1,3},[0-9]{1,3}\)"
    # matches = re.findall(pattern, "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))")
    matches = re.findall(pattern, file.read())
    total = 0
    for match in matches:
        total += eval(match)
    print("Day 3 - Part 1 :", total)


def part2(file):
    data = re.split("(do\(\)|don't\(\))", file.read())
    # data = re.split("(do\(\)|don't\(\))", "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))")
    total = 0
    pattern = r"mul\([0-9]{1,3},[0-9]{1,3}\)"
    do = True
    for inst in data:
        if inst == "do()": 
            do = True
            continue
        elif inst == "don't()":
            do = False
            continue

        if do:
            matches = re.findall(pattern, inst)
            for match in matches:
                total += eval(match)
    print("Day 3 - Part 2: ", total)




def main():
    file = open("inputs/day3.txt")
    if sys.argv[1] == "1":
        part1(file)
    elif sys.argv[1] == "2":
        part2(file)

if __name__ == "__main__":
    main()