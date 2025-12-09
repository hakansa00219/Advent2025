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


# geometry helpers (robust)
def orient(a, b, c):
    # cross product (b-a) x (c-a)
    return (b[0]-a[0])*(c[1]-a[1]) - (b[1]-a[1])*(c[0]-a[0])

def on_segment(a, b, c):
    # is point c on segment ab? (inclusive)
    return (min(a[0], b[0]) <= c[0] <= max(a[0], b[0]) and
            min(a[1], b[1]) <= c[1] <= max(a[1], b[1]))

def seg_intersect(a, b, c, d):
    # robust segment intersection (handles colinear & endpoints)
    o1 = orient(a,b,c)
    o2 = orient(a,b,d)
    o3 = orient(c,d,a)
    o4 = orient(c,d,b)

    # General case
    if o1 == 0 and on_segment(a,b,c): return True
    if o2 == 0 and on_segment(a,b,d): return True
    if o3 == 0 and on_segment(c,d,a): return True
    if o4 == 0 and on_segment(c,d,b): return True

    return (o1 > 0) != (o2 > 0) and (o3 > 0) != (o4 > 0)


# point-in-polygon (ray casting) but return True if point is on any edge
def point_on_polygon_edge(x, y, poly):
    n = len(poly)
    for i in range(n):
        a = poly[i]
        b = poly[(i+1) % n]
        if orient(a, b, (x,y)) == 0 and on_segment(a, b, (x,y)):
            return True
    return False

def point_in_polygon(x, y, poly):
    # if exactly on edge/vertex -> consider inside (changeable)
    if point_on_polygon_edge(x, y, poly):
        return True

    inside = False
    n = len(poly)
    for i in range(n):
        x1, y1 = poly[i]
        x2, y2 = poly[(i+1) % n]

        # check if edge crosses the horizontal ray to the right of (x,y)
        if ((y1 > y) != (y2 > y)):
            # compute x coordinate of intersection
            xinters = x1 + (y - y1) * (x2 - x1) / (y2 - y1)
            if x < xinters:
                inside = not inside
    return inside


# rectangle helpers (axis-aligned)
def rect_corners_from_two(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    xmin, xmax = min(x1, x2), max(x1, x2)
    ymin, ymax = min(y1, y2), max(y1, y2)
    # return in order A,B,C,D (clockwise)
    return [(xmin, ymin), (xmax, ymin), (xmax, ymax), (xmin, ymax)]

def rect_edges_from_corners(corners):
    return [(corners[i], corners[(i+1) % 4]) for i in range(4)]


def is_rect_inside_polygon(e1,e2,e3,e4, poly):
    # 1) check corners inside (treat boundary as inside)
    for (x, y) in [e1,e2,e3,e4]:
        if not point_in_polygon(x, y, poly):
            return False
    return True
"""
    # 2) check any rectangle edge intersects any polygon edge
    rect_edges = [(e1,e2),(e2,e3),(e3,e4),(e4,e1)]
    n = len(poly)
    for re_a, re_b in rect_edges:
        for i in range(n):
            p1 = poly[i]
            p2 = poly[(i+1) % n]
            if seg_intersect(re_a, re_b, p1, p2):
                # if the only intersection is at a shared corner (touching at polygon vertex),
                # decide policy: here we treat touching as NOT allowed (so return False).
                # If you want touching allowed, you should check whether intersection point is exactly at rectangle corner
                return False
"""

