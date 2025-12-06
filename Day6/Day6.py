from input_loader import load_input
import re
from itertools import zip_longest

text = load_input("input.txt")

part1 = 0
part2 = 0

numPattern = "[0-9]+"
operatorPattern = r"\S"
numses = []

lines = text.splitlines()

#part1
for i,line in enumerate(lines):
    if i != len(lines)-1:
        numses.append(re.findall(numPattern, lines[i]))

operators = re.findall(operatorPattern,lines[-1])

for i, operator in enumerate(operators):
    verticalTotal = 0
    for nums in numses:
        match operator:
            case "+":
                verticalTotal += int(nums[i])
            case "*":
                verticalTotal = (verticalTotal if verticalTotal != 0 else 1) * int(nums[i])

    part1 += verticalTotal

#part2
groups = list(zip_longest(*lines[:-1], fillvalue=' '))[::-1]
operatorIndex = 0
total = 0
for i, group in enumerate(groups):
    if all(x == ' ' for x in group):
        operatorIndex += 1
        part2 += total
        total = 0
        continue
    num = re.search("\S+","".join(group)).group()
    match operators[-operatorIndex - 1]:
        case "+":
            total += int(num)
        case "*":
            total = (total if total != 0 else 1) * int(num)

if total != 0:
    part2 += total
    total = 0

#print(groups)
print("Part1:" + str(part1))
print("Part2:" + str(part2))