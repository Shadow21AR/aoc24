import sys

def part1(rows):
    rLen = len(rows)
    cLen = len(rows[0])
    total = 0
    for r in range(rLen):
        for c in range(cLen):
            if rows[r][c] != "X":
                continue
            total += sum([c > 2 and rows[r][c-3:c+1] == "SAMX"])
            total += sum([c < cLen - 3 and rows[r][c:c+4] == "XMAS"])
            total += sum([r > 2 and ''.join(rows[r-i][c] for i in range(4)) == "XMAS"])
            total += sum([r < rLen - 3 and ''.join(rows[r+i][c] for i in range(4)) == "XMAS"])
            total += sum([c > 2 and r > 2 and ''.join(rows[r-i][c-i] for i in range(4)) == "XMAS"])
            total += sum([c > 2 and r < rLen - 3 and ''.join(rows[r+i][c-i] for i in range(4)) == "XMAS"])
            total += sum([c < cLen -3 and r > 2 and ''.join(rows[r-i][c+i] for i in range(4)) == "XMAS"])
            total += sum([c < cLen -3 and r < rLen - 3 and ''.join(rows[r+i][c+i] for i in range(4)) == "XMAS"])
    print("Day 4 - Part 1: ", total)
    
def part2(rows):
    rLen = len(rows)
    cLen = len(rows[0])
    total = 0
    for r in range(1, rLen - 1):
        for c in range(1, cLen - 1):
            diagonal1 = ''.join(rows[r + i][c + i] for i in [-1, 0, 1]) 
            diagonal2 = ''.join(rows[r - i][c + i] for i in [-1, 0, 1]) 
            
            if diagonal1 in ("MAS", "SAM") and diagonal2 in ("MAS", "SAM"):
                total += 1
    print("Total:", total)

def main():
    input = open("inputs/day4.txt").read().strip().split("\n")

    if sys.argv[1] == "1":
        part1(input)
    elif sys.argv[1] == "2":
        part2(input)

if __name__ == "__main__":
    main()