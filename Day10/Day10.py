import math

from tqdm import tqdm
import time
from utils import flatten_and_sort
from input_loader import load_input
from itertools import combinations, product
import re

text = load_input("input.txt")

part1 = 0
part2 = 0

machines = text.split('\n')
pattern = "[\(\[\{](.*?)[\)\]\}]"

start = time.perf_counter()
ind = 0
for machine in tqdm(machines, desc="Lighting up", position=0):
    groups = re.findall(pattern, machine)
    lights = groups[0]
    joltages = list(map(int, groups[-1].split(',')))
    buttons = [list(map(int, item.split(','))) for item in groups[1:-1]]

    # PART 1
    patternLength = 1
    found = False
    while not found:
        samples = combinations(buttons, patternLength)
        for sample in samples:
            if patternLength == 1:
                sample = sample[0]
            initLights = lights
            cleaned_sample = flatten_and_sort(sample)
            for ch in cleaned_sample:
                initLights = initLights[:ch] + ('#' if initLights[ch] == '.' else '.') + initLights[ch + 1:]
            if initLights.count('.') == len(initLights):
                found = True
                break
        else:
            patternLength += 1
    part1 += patternLength

    # PART 2

    jolt_count = len(joltages)
    max_use = max(joltages)
    move_count = len(buttons)
    best = math.inf
    best_combo = None
    moves = buttons
    total = 0
    isSkippable = False
    while True:
        index_count_lookup = {}

        for c in range(jolt_count):
            if joltages[c] == 0:
                continue
            indexes = [i for i, sub in enumerate(moves) if c in sub]
            index_count_lookup.setdefault(c, indexes)

        one_element_count = 0
        for i in index_count_lookup:
            if len(index_count_lookup[i]) == 1:
                one_element_count += 1
                total += joltages[i]
                for _ in range(joltages[i]):
                    for index in moves[index_count_lookup[i][0]]:
                        joltages[index] -= 1
        if one_element_count == 0:
            break

        if all(joltages[i] == 0 for i in range(jolt_count)):
            part2 += total
            isSkippable = True
            break

        for i, joltage in enumerate(joltages):
            if joltage == 0:
                moves = [sub for sub in moves if i not in sub]

    if isSkippable:
        ind += 1
        continue
    if (max_use + 1) ** move_count > 10000000:
        continue
    with tqdm(total = (max_use + 1) ** move_count, desc="Brute forcing", position=1, leave=False) as pbar:
        for combo in product(range(max_use + 1), repeat = move_count):
            reducing = [0]*jolt_count
            for move_idx, times in enumerate(combo):
                if times == 0:
                    continue
                for idx in buttons[move_idx]:
                    reducing[idx] += times
            if reducing == joltages:
                total = sum(combo)
                if best is None or total < best:
                    best = total
                    best_combo = combo
            pbar.update(1)

    part2 += best



end = time.perf_counter()
print(str(ind) + " of them optimized")
print("Part1:" + str(part1))
print("Part2:" + str(part2))
print("Duration: " + str(end - start) + " s")
print("Duration: " + str((end - start) * 1000)  + " ms")