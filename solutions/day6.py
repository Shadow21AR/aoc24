import copy

directions = {
    (-1, 0): [0, 1],
    (0, 1): [1, 0],
    (1, 0): [0, -1],
    (0, -1): [-1, 0]
}

def findPos(input, curPos):
    for row in range(len(input)):
        try:
            index = input[row].index("^")
            curPos.update({"x": row, "y":index})
            break
        except:
            pass
    return curPos

def runParts(input):
    origInput = copy.deepcopy(input)
    curPos = findPos(input, {"x":0, "y":0})
    curDir = [-1, 0]
    pd = curDir
    visited = {}
    while True:
        (x , y)= curPos.values()
        input[x][y] = "X"
        key = (x,y, curDir[0], curDir[1])
        visited[key] = {"px": x - curDir[0], "py": y - curDir[1], "pd": pd}
        nextPos = {"x": x + curDir[0], "y": y + curDir[1]}
        if 0 <= curPos["x"] < len(input)-1 and 0 <= curPos["y"] < len(input[0])-1:
            if input[nextPos["x"]][nextPos["y"]] == "#":
                curDir = directions[tuple(curDir)]
                nextPos = {"x": x + curDir[0], "y": y + curDir[1]}
            visited[key].update({"nx": nextPos["x"], "ny": nextPos["y"], "nd": curDir})
        else:
            visited[key].update({"nx": nextPos["x"], "ny": nextPos["y"], "nd": curDir})
            break
        curPos = nextPos
        pd = curDir
    total = 0
    for row in range(len(input)):
        for col in range(len(input[0])):
            if input[row][col] == "X": total += 1
    print("Day 6 - Part 1 : ", total-1) # :c
    part2(origInput, visited)

def part2(input,visited): # doesn't work on real input but whatever i gave up
    total = 0
    loop = 0
    for k,v in visited.items():
        checked = {}
        curPos = {"x": k[0], "y": k[1]}
        curDir = [k[2], k[3]]
        (x , y)= curPos.values()
        if v["nx"] >= len(input) or v["ny"] >= len(input[0]): break
        if not tuple([curPos["x"], curPos["y"], curDir[0], curDir[1]]) in checked:
            input[v["nx"]][v["ny"]] = "#"
        checked[tuple([curPos["x"], curPos["y"], curDir[0], curDir[1]])] = True
        for i in range(17000): # i think it is enough loop.
            nextPos = {"x": curPos["x"] + curDir[0], "y": curPos["y"] + curDir[1]}
            if 0 <= curPos["x"] < len(input)-1 and 0 <= curPos["y"] < len(input[0])-1:
                if input[nextPos["x"]][nextPos["y"]] == "#":
                    curDir = directions[tuple(curDir)]
                    nextPos = {"x": curPos["x"] + curDir[0], "y": curPos["y"] + curDir[1]}
            else:
                input[v["nx"]][v["ny"]] = "."
                break
            curPos = nextPos
            if tuple([curPos["x"], curPos["y"], curDir[0], curDir[1]]) == k: 
                loop += 1
            if loop >= 2:
                total += 1
                input[v["nx"]][v["ny"]] = "."
                loop = 0
                break
        input[v["nx"]][v["ny"]] = "."
    print("Day 6 - Part 2 : ", total, "[Wrong]")

def main():
    input = [[col for col in list(row.strip())] for row in open("inputs/day6.txt").read().strip().split("\n")]
#     input = [[col for col in list(row.strip())] for row in """....#.....
# .........#
# ..........
# ..#.......
# .......#..
# ..........
# .#..^.....
# ........#.
# #.........
# ......#...""".strip().split("\n")]
    
    runParts(input)


if __name__ == "__main__":
    main()