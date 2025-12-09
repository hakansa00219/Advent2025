def print_grid(g):
    for gridPart in g:
        print("  ".join(gridPart))
def grid_borders(nums, g):
    for i in range(len(nums)):
        a = nums[i]
        b = nums[(i + 1) % len(nums)]
        if a[0] == b[0]:
            if b[1] > a[1]:
                diff = b[1] - a[1]
                for j in range(diff - 1):
                    g[a[1] + j + 1][a[0]] = 'X'
            else:
                diff = a[1] - b[1]
                for j in range(diff - 1):
                    g[b[1] + j + 1][b[0]] = 'X'

        elif a[1] == b[1]:
            if b[0] > a[0]:
                diff = b[0] - a[0]
                for j in range(diff - 1):
                    #8,1 9,1 10,1
                    g[a[1]][a[0] + j + 1] = 'X'
            else:
                diff = a[0] - b[0]
                for j in range(diff - 1):
                    g[b[1]][b[0] + j + 1] = 'X'

def is_inside(x, y, g):

    if g[y][x] == 'X' or g[y][x] == '#':
        return True

    border_count = 0
    size = len(g[0])
    count = size - x
    for i in range(count - 1):
        ch = g[y][x + i + 1]
        if ch == 'X' or ch == '#':
            border_count += 1

    print(str(x) + "," + str(y) + " - " + str(border_count))
    return border_count == 1