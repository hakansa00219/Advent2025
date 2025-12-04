import math

from input_loader import load_input

text = load_input("input.txt")

lines = [list(line) for line in text.split("\n")]

part1 = 0
part2 = 0

positions = []

def check_adj_papers():
    left = 0
    for i, line in enumerate(lines):
        for j, char in enumerate(line):
            if char != '@':
                continue

            adjPaperCount = 0

            if i != 0:  # check 3 ups
                adjPaperCount += 1 if lines[i - 1][j] == '@' else 0
                adjPaperCount += 1 if j > 0 and lines[i - 1][j - 1] == '@' else 0
                adjPaperCount += 1 if j < len(line) - 1 and lines[i - 1][j + 1] == '@' else 0
            if i != len(lines) - 1:  # check 3 downs
                adjPaperCount += 1 if lines[i + 1][j] == '@' else 0
                adjPaperCount += 1 if j > 0 and lines[i + 1][j - 1] == '@' else 0
                adjPaperCount += 1 if j < len(line) - 1 and lines[i + 1][j + 1] == '@' else 0
            if j != 0:  # check 1 left mid
                adjPaperCount += 1 if lines[i][j - 1] == '@' else 0
            if j != len(line) - 1:  # check 1 right mid
                adjPaperCount += 1 if lines[i][j + 1] == '@' else 0

            if adjPaperCount < 4:
                left += 1
                positions.append((i, j))



    return left

left = math.inf
once = False
while 1:
    #print(left)
    if left != 0 :
        left = check_adj_papers()

        if not once:
            part1 += left
            print("Part1:" + str(part1))
            once = True

        for i, position in enumerate(positions):
            lines[position[0]][position[1]] = '.'

        part2 += left
    else:
        break






print("Part2:" + str(part2))