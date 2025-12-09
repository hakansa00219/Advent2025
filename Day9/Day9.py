from sympy.physics.units import second

from input_loader import load_input
from grid_utility import *
text = load_input("input.txt")

part1 = 0
part2 = 0

lines = text.split('\n')

nums = [tuple(map(int, line.split(','))) for line in lines]
maxNum = max(max(nums)[0],max(nums)[1])
print(nums)
grid = [['.' for _ in range(maxNum + 1)] for _ in range(maxNum + 1)]
for num in nums:

    grid[num[1]][num[0]] = '#'

grid_borders(nums, grid)
print_grid(grid)

biggestArea_part1 = 0
biggestArea_part2 = 0
for i in range(len(nums)):
    for j in range(i + 1, len(nums)):

        firstRedTile = nums[i]
        secondRedTile = nums[j]

        edge1 = (firstRedTile[0], secondRedTile[1])
        edge2 = (secondRedTile[0], firstRedTile[1])

        area = (abs(secondRedTile[0] - firstRedTile[0]) + 1) * (abs(secondRedTile[1] - firstRedTile[1]) + 1)
        if area > biggestArea_part1:
            biggestArea_part1 = area
        if is_inside(edge1[0], edge1[1], grid) and is_inside(edge2[0], edge2[1], grid) and area > biggestArea_part2:
            biggestArea_part2 = area

part1 = biggestArea_part1
part2 = biggestArea_part2

print("Part1:" + str(part1))
print("Part2:" + str(part2))