from input_loader import load_input

text = load_input("input.txt")

idsRanges = text.split(',')

part1 = 0
part2 = 0

# 123123
# get number count = 6
# split into two halves
# check if first half matches second half
# if true invalid add to part1
# next number

for ids in idsRanges:
    ids = ids.split('-')
    start = int(ids[0])
    end = int(ids[1])

    current = start
    while 1:
        currentStr = str(current)
        numberCount = len(currentStr)
        if currentStr[0:(numberCount//2)] == currentStr[(numberCount//2):numberCount]:
            print("Invalid ID: " + currentStr)
            part1 += current

        if current == end:
            break

        current += 1




print("Part1:" + str(part1))
print("Part2:" + str(part2))