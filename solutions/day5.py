import sys

def parseInput(input):
    pages = {}
    data = input.strip().split("\n\n")
    for page in data[0].split("\n"):
        temp = page.split("|")
        if int(temp[0]) not in pages:
            pages[int(temp[0])] = []
        pages[int(temp[0])].append (int(temp[1]))
    updates = [[int(x) for x in update.split(",")] for update in data[1].split("\n")]
    
    return pages, updates


def solve(pages, updates):
    total = 0
    incorrect = []
    for update in updates:
        ordered = True
        for x in range(len(update)):
            toCheck = update[x+1:]
            if update[x] not in pages:
                continue
            ordered = all(item in pages[update[x]] for item in toCheck) and all(item not in pages[update[x]] for item in update[:x])
            if not ordered:
                incorrect.append(update)
                break
        if ordered:
            total += update[len(update) //2]
    print("Day 5 - Part 1: ",total)
    total2 = 0
    fixed = []
    for update in incorrect:
        temp = []
        i = 0
        while len(temp) != len(update):
            if update[i] not in pages:
                pages[update[i]] = [9999999999] # :c
                continue
                
            if update[i] in temp:
                i = (i + 1) % len(update)
                continue
            
            toCheck = [n for n in update if n != update[i] and n not in temp]
            pageRule = pages[update[i]]
            ordered = all(item in pageRule for item in toCheck) and all(item not in pageRule for item in temp)
            # print(f"Num: {update[i]}\nRule: {pageRule}\nToCheck: {toCheck}\nOnLeft: {temp}\nOrdered: {ordered}\nTemp: {temp}\n\n")
            
            if ordered:
                temp.append(update[i])
                
            i = (i + 1) % len(update)
            
        fixed.append(temp)
        
    print("Day 5 - Part 2: ", sum([r[len(r) //2] for r in fixed]))

def main():
    input = open("inputs/day5.txt").read()
    pages, updates = parseInput(input)
    solve(pages,updates)

if __name__ == "__main__":
    main()