from input_loader import load_input

text = load_input("input.txt")

lines = text.split("\n")

part1 = 0
part2 = 0

for i, line in enumerate(lines):

    for j, char in enumerate(line):
        if char != '@':
            continue

        adjPaperCount = 0

        if i != 0: #check 3 ups
            adjPaperCount += 1 if lines[i - 1][j] == '@' else 0
            adjPaperCount += 1 if j > 0 and lines[i - 1][j - 1] == '@' else 0
            adjPaperCount += 1 if j < len(line) - 1 and lines[i - 1][j + 1] == '@' else 0
        if i != len(lines) - 1: #check 3 downs
            adjPaperCount += 1 if lines[i + 1][j] == '@' else 0
            adjPaperCount += 1 if j > 0 and lines[i + 1][j - 1] == '@' else 0
            adjPaperCount += 1 if j < len(line) - 1 and lines[i + 1][j + 1] == '@' else 0
        if j != 0: #check 1 left mid
            adjPaperCount += 1 if lines[i][j - 1] == '@' else 0
        if j != len(line) - 1: #check 1 right mid
            adjPaperCount += 1 if lines[i][j + 1] == '@' else 0


        if adjPaperCount < 4:
            part1 += 1




print("Part1:" + str(part1))
print("Part2:" + str(part2))