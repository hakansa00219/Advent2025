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

startInput = 'svr'
firstEncounter = 'fft'
secondEncounter = 'dac'
endOutput = 'out'



for i,line in enumerate(lines):
    groups = re.findall(expression, line)
    input = groups[0]  # left side "aaa"
    outputs = groups[1:]  # right side "you","hhh"

    lookup.setdefault(input, outputs)

    if input == startInput:
        startIndex = i

pbar = tqdm()
valueCache = {}
valueCache.setdefault(endOutput, 0)
outCache = {}
outCache.setdefault(endOutput, 1)
stack = []
stack.append((startInput, [startInput], False, None))
while len(stack) > 0:
    input, path, visited, dac, *rest  = stack.pop()
    pbar.update(1)
    print(path)

    if input in valueCache:
        continue

    if not visited:
        if input == endOutput:
            continue
        outputs = lookup[input]
        dacInPath = True if secondEncounter in path else False
        endOutputInOutputs = True if endOutput in outputs else False
        stack.append((input, path, True, dacInPath , outputs))
        for output in outputs:
            outputPath = list(path)
            outputPath.append(output)
            childDac = dac or (input == secondEncounter)
            stack.append((output, outputPath, False, childDac))
    else:
        total = 0
        outCountTotal = 0
        rest = rest[0]
        for r in rest:
            total += valueCache.get(r)
            if dac:
                outCountTotal += valueCache.get(r, 0)

        valueCache.setdefault(input, total + 1  if input == firstEncounter else total)
        outCache.setdefault(input, outCountTotal)
        continue

print(str(outCache.get(startInput)) + " - " + str(valueCache.get(startInput)))
# find "you" line
# iterate through connections
# stack data design with caches while iterating through (dfs)
# when you see "out" part1++ and continue with stack


print("Part1:" + str(part1))
print("Part2:" + str(part2))