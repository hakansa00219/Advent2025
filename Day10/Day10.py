from tqdm import tqdm
import time
from utils import flatten_and_sort
from input_loader import load_input
from itertools import combinations
import re

text = load_input("input.txt")

part1 = 0
part2 = 0

machines = text.split('\n')
pattern = "[\(\[\{](.*?)[\)\]\}]"

start = time.perf_counter()
for machine in tqdm(machines, desc="Lighting up"):
    groups = re.findall(pattern, machine)
    lights = groups[0]
    joltages = list(map(int, groups[-1].split(',')))
    buttons = [list(map(int, item.split(','))) for item in groups[1:-1]]

    shortestPattern = []
    patternLength = 1
    while len(shortestPattern) == 0:
        found = False
        samples = combinations(buttons, patternLength)
        for sample in samples:
            if patternLength == 1:
                sample = sample[0]
            initLights = lights
            cleaned_sample = flatten_and_sort(sample)
            #for s in sample:
            for ch in cleaned_sample:
                initLights = initLights[:ch] + ('#' if initLights[ch] == '.' else '.') + initLights[ch + 1:]
            if initLights.count('.') == len(initLights):
                shortestPattern = sample
                found = True
                break
        if found:
            break
        else:
            patternLength += 1
    part1 += patternLength

end = time.perf_counter()
print("Part1:" + str(part1))
print("Part2:" + str(part2))
print("Duration: " + str(end - start) + " s")
print("Duration: " + str((end - start) * 1000)  + " ms")