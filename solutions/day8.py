import sys

class Grid:
    def __init__(self, data):
        self.grid = [list(row) for row in data.splitlines()]
        self.rows = len(self.grid)
        self.cols = len(self.grid[0]) if self.grid else 0

    def get(self, row, col):
        if 0 <= row < self.rows and 0 <= col < self.cols:
            return self.grid[row][col]
        return None

    def set(self, row, col, value):
        self.grid[row][col] = value

    def check(self, row, col):
        char = self.grid[row][col]
        out = {(row,col): []}
        for r in range(len(self.grid)):
            for c in range(len(self.grid[row])):
                if self.grid[row][col] != "." and self.grid[r][c] == char and row != r and col != c:
                    out[(row,col)].append([r,c])
        return out

    def markAN(self, ant, row, col):
        disX = abs(ant[0] - row)
        disY = abs(ant[1] - col)
        if ant[0] > row:
            disX *= -1
        if ant[1] > col:
            disY *= -1
        antiNode = [row+disX, col+disY]
        if 0 <= antiNode[0] < self.rows and 0 <= antiNode[1] < self.cols:
            self.grid[antiNode[0]][antiNode[1]] = "#"
        return self.grid
    
    def markANHarmonics(self, ant, row, col):
        disX = abs(ant[0] - row)
        disY = abs(ant[1] - col)
        if ant[0] > row:
            disX *= -1
        if ant[1] > col:
            disY *= -1
        antiNode = [row+disX, col+disY]
        if 0 <= antiNode[0] < self.rows and 0 <= antiNode[1] < self.cols:
            self.grid[antiNode[0]][antiNode[1]] = "#"
            self.markANHarmonics((row, col), antiNode[0], antiNode[1])
        else:
            return self.grid
    
    def checkAntiNodes(self):
        return sum(row.count("#") for row in self.grid)
    
    def checkAntiNodesWithHarmonic(self):
        total = sum(len(row) for row in self.grid)
        dots = sum(row.count(".") for row in self.grid)
        return total - dots

    def __str__(self):
        return "\n".join("".join(row) for row in self.grid)

def part1(area):
    res = {}
    for r in range(area.rows):
        for c in range(area.cols):
            if area.get(r,c) != ".":
                out = area.check(r,c)
                for k,v in out.items():
                    for pair in v:
                        res.setdefault(k, []).append(pair)
    for k,v in res.items():
        for x,y in v:
            area.markAN(k,x,y)
    print("Day 8 - Part 1 : ", area.checkAntiNodes())

def part2(area):
    res = {}
    for r in range(area.rows):
        for c in range(area.cols):
            if area.get(r,c) != ".":
                out = area.check(r,c)
                for k,v in out.items():
                    for pair in v:
                        res.setdefault(k, []).append(pair)
    for k,v in res.items():
        for x,y in v:
            area.markANHarmonics(k,x,y)
    print("Day 8 - Part 2 : ", area.checkAntiNodesWithHarmonic())

def main():
    data = open("inputs/day8.txt").read().strip()
#     data = """............
# ........0...
# .....0......
# .......0....
# ....0.......
# ......A.....
# ............
# ............
# ........A...
# .........A..
# ............
# ............""".strip()
    area = Grid(data)
    if sys.argv[1] == "1":
        part1(area)
    elif sys.argv[1] == "2":
        part2(area)

if __name__ == "__main__":
    main()