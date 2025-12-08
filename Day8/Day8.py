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
part1_iteration = 1000
i = 0
while True:
    dist, a, b = closest_boxes[i]
    a = tuple(map(int, a.split(',')))
    b = tuple(map(int, b.split(',')))
    dsu.union(a, b)
    print(i)
    i += 1
    components = {}
    for coord in coords:
        root = dsu.find(coord)
        components.setdefault(root, []).append(coord)

    if i == part1_iteration:
        circuits = list(components.values())
        counts = [len(circuit) for circuit in circuits]
        counts.sort(reverse=True)
        part1 = math.prod(counts[:3])

    if len(components) == 1:
        print(a)
        print(b)
        part2 = int(a[0]) * int(b[0])
        break;

circuits = list(components.values())
for c in circuits:
    print(c)


print("Part1:" + str(part1))
print("Part2:" + str(part2))