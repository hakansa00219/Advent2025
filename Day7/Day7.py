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
print("Part2:" + str(part2))