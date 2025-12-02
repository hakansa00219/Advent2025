from input_loader import load_input
from sympy import divisors

text = load_input("input.txt")

idsRanges = text.split(',')

part1 = 0
part2 = 0
# part1
# 123123
# get number count = 6
# split into two halves
# check if first half matches second half
# if true invalid add to part1
# next number
# part2
# number count get all divisions
# check if divided parts by division matches

for ids in idsRanges:
    ids = ids.split('-')
    start = int(ids[0])
    end = int(ids[1])

    current = start
    while 1:
        currentStr = str(current)
        numberCount = len(currentStr)
        divs = (divisors(numberCount))
        divs.remove(numberCount) # number 123123 -> divs = [1,2,3] self removed
        for i, div in enumerate(divs): # div 1 -> 1 2 not equals continue
                                       # div 2 -> 12 31 not equals continue
                                       # div 3 -> 123 123 equals invalid add to part2
            slices = [currentStr[j:j + div] for j in range(0, numberCount, div)]
            isAllEquals = all(x == slices[0] for x in slices)

            if not isAllEquals:
                continue # with next division

            # all equals - invalid
            part2 += current
            break # continue with next number

        if currentStr[0:(numberCount//2)] == currentStr[(numberCount//2):numberCount]:
            #print("Invalid ID: " + currentStr)
            part1 += current

        if current == end:
            break

        current += 1




print("Part1:" + str(part1))
print("Part2:" + str(part2))