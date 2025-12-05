from input_loader import load_input

text = load_input("input.txt")

part1 = 0
part2 = 0

lines = text.split('\n')
empty_line_index = lines.index('')
fresh_ings = lines[0:empty_line_index]
available_ings = [int(x) for x in lines[empty_line_index+1:]]

print(fresh_ings)
print(available_ings)




for available_ing in available_ings:
    for ingRanges in fresh_ings:
        ranges = ingRanges.split('-')
        start = int(ranges[0])
        end = int(ranges[1])

        if start <= available_ing <= end:
            # fresh
            part1 += 1
            break

print("Part1:" + str(part1))
print("Part2:" + str(part2))