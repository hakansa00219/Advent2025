import re
import sys

import input_loader

*shapes, regions = input_loader.load_input("input.txt").strip().split('\n\n')

regions = [
    list(map(int, re.findall(r'\d+', region)))
        for region in regions.split('\n')
]

def fail():
    assert False, "Failed to determine if presents fit under tree."

print("Part 1:", sum(
         1      if (w // 3) * (h // 3) >= sum(nums)
    else 0      if sum(num*shape.count('#') for num, shape in zip(nums, shapes)) > w * h
    else fail()
        for w, h, *nums in regions
))