from splitter import Splitter
from input_loader import load_input

text = load_input("input.txt")

part1 = 0
part2 = 0

lines = text.split("\n")
startIndex = lines[0].index('S')
stack = [(0, startIndex)]
alreadyBeamed = []

while len(stack) > 0:
    current = stack.pop()
    x = current[1]
    y = current[0]

    if lines[y][x] == '^':
        # split
        if not (y, x + 1) in alreadyBeamed:
            stack.append((y, x + 1))
            alreadyBeamed.append((y, x + 1))
        if not (y, x - 1) in alreadyBeamed:
            stack.append((y, x - 1))
            alreadyBeamed.append((y, x - 1))

        part1 += 1
    else:
        if not (y + 1, x) in alreadyBeamed:
            stack.append((y + 1, x))
            alreadyBeamed.append((y + 1, x))

    if y == len(lines) - 1:
        stack.pop()

print("Part1:" + str(part1))
beamStack = [("DO", 0, startIndex)]
cache = {}

while beamStack:
    process, y, x, *rest = beamStack.pop()

    if process == "DO":

        if y == len(lines) - 1:
            cache[(y, x)] = 1
            part2 += 1
            continue

        c = lines[y][x]

        if c == '^':
            left = (y, x - 1)
            right = (y, x + 1)

            # cache skip
            if (y, x) in cache:
                val = cache.get(left, 0) + cache.get(right, 0)
                continue

            #parent merge
            beamStack.append(("MERGE_SPLIT", y, x, left, right))

            #children
            beamStack.append(("DO", right[0], right[1]))
            beamStack.append(("DO", left[0], left[1]))

        else:
            down = (y + 1, x)

            #cache skip
            if (y, x) in cache:
                val = cache.get(down, 0)

            #down
            beamStack.append(("MERGE_DOWN", y, x, down))
            beamStack.append(("DO", down[0], down[1]))

    elif process == "MERGE_SPLIT":
        left,right = rest
        val = cache.get(left, 0) + cache.get(right, 0)
        cache[(y,x)] = val

    elif process == "MERGE_DOWN":
        (down, ) = rest
        val = cache.get(down, 0)
        cache[(y,x)] = val


print("Part2:" + str(cache.get((0, startIndex))))

