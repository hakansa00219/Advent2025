import math
from tqdm import tqdm
import time
from input_loader import load_input
import re

text = load_input("input.txt")

part1 = 0
part2 = 0

lines = text.splitlines()
expression = "[a-z]{3}"

#create cache lookup
lookup = {}
startIndex = None



for i,line in enumerate(lines):
    groups = re.findall(expression, line)
    input = groups[0]  # left side "aaa"
    outputs = groups[1:]  # right side "you","hhh"

    lookup.setdefault(input, outputs)

    if input == "you":
        startIndex = i


stack = []
stack.append('you')

while len(stack) > 0:
    current = stack.pop()
    if current == 'out':
        part1 += 1
    if current in lookup:
        outputs = lookup[current]
        for output in outputs:
            stack.append(output)



# find "you" line
# iterate through connections
# stack data design with caches while iterating through (dfs)
# when you see "out" part1++ and continue with stack


print("Part1:" + str(part1))
print("Part2:" + str(part2))