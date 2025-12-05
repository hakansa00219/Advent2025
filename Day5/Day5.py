import math

from mpmath.math2 import cotpi

from input_loader import load_input

text = load_input("input.txt")

part1 = 0
part2 = 0

lines = text.split('\n')
empty_line_index = lines.index('')
fresh_ings = lines[0:empty_line_index]
available_ings = [int(x) for x in lines[empty_line_index+1:]]


points = set()

for available_ing in available_ings:
    for ingRanges in fresh_ings:
        ranges = ingRanges.split('-')
        start = int(ranges[0])
        end = int(ranges[1])

        if start <= available_ing <= end:
            # fresh
            part1 += 1
            break

for ranges in fresh_ings:
    range = ranges.split('-')
    start = int(range[0])
    end = int(range[1])

    points.add(start)
    points.add(end)

sortedPoints = sorted(points)

freshList = set()

for i, sortedPoint in enumerate(sortedPoints):
    a = sortedPoints[i]
    if a == sortedPoints[-1]:
        break
    b = sortedPoints[i+1]

    for ranges in fresh_ings:
        range = ranges.split('-')
        start = int(range[0])
        end = int(range[1])

        if start <= a and b <= end:
            freshList.add((a, b))

freshList = list(freshList)
while True:
    freshList.sort()
    merged = []
    changed = False

    for s, e in freshList:
        if not merged:
            merged.append([s, e])
            continue

        last_s, last_e = merged[-1]

        if s <= last_e + 1:
            merged[-1][1] = e
            changed = True
        else:
            merged.append([s, e])

    if not changed:
        freshList = merged
        break


    freshList = merged

for s, e in freshList:
    part2 += (e - s + 1)

print(sorted(freshList))

print("Part1:" + str(part1))
print("Part2:" + str(part2))