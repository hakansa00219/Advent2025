from input_loader import load_input

text = load_input("input.txt")

currentDial = 50
part1 = 0
part2 = 0
splitText = text.split('\n')
counter = 0
for line in splitText:
    counter += 1
    rotation = line[0]
    degrees = int(line[1:])
    while degrees != 0:
        currentDial += -1 if rotation == 'L' else 1
        degrees -= 1
        if currentDial == 100:
            currentDial = 0
        elif currentDial == -1:
            currentDial = 99

        if currentDial == 0 and degrees != 0:
            part2 += 1

    if currentDial == 0:
        part1 += 1

part2 += part1
print("Part1:" + str(part1))
print("Part2:" + str(part2))