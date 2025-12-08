import math

from DSU import DSU
from input_loader import load_input

text = load_input("input.txt")

part1 = 0
part2 = 0

junction_boxes = text.split("\n")

coords = [tuple(map(int, box.split(","))) for box in junction_boxes]

closest_boxes = []

for i in range(len(coords)):
    for j in range(i + 1, len(coords)):
        x1,y1,z1 = coords[i]
        x2,y2,z2 = coords[j]

        dist = math.dist(coords[i], coords[j])

        closest_boxes.append((dist, junction_boxes[i], junction_boxes[j]))

closest_boxes.sort(key=lambda x: x[0])
print(*closest_boxes[:10], sep='\n')

dsu = DSU()
iteration = 1000

for i in range(min(iteration, len(closest_boxes))):
    dist, a, b = closest_boxes[i]
    a = tuple(map(int, a.split(',')))
    b = tuple(map(int, b.split(',')))
    dsu.union(a, b)

components = {}
for point in coords:
    root = dsu.find(point)
    components.setdefault(root, []).append(point)

circuits = list(components.values())
for c in circuits:
    print(c)

counts = [len(circuit) for circuit in circuits]
counts.sort(reverse=True)
part1 = math.prod(counts[:3])
print(counts, sep='\n')


print("Part1:" + str(part1))
print("Part2:" + str(part2))