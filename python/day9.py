heights = []
with open("day9.txt") as f:
    for line in f:
        heights.append([int(x) for x in line.strip()])


def get_neighbours_coord(x, y, heights):
    if x == 0:
        if y == 0:
            return [
                (1, 0),
                (0, 1),
            ]
        elif y == len(heights) - 1:
            return [
                (y - 1, 0),
                (y, 1),
            ]
        else:
            return [
                (y - 1, 0),
                (y, 1),
                (y + 1, 0),
            ]
    elif x == len(heights[0]) - 1:
        if y == 0:
            return [
                (1, x),
                (0, x - 1),
            ]
        elif y == len(heights) - 1:
            return [
                (y - 1, x),
                (y, x - 1),
            ]
        else:
            return [
                (y - 1, x),
                (y, x - 1),
                (y + 1, x),
            ]
    elif y == 0:
        return [
            (0, x - 1),
            (1, x),
            (0, x + 1),
        ]
    elif y == len(heights) - 1:
        return [
            (y, x - 1),
            (y - 1, x),
            (y, x + 1),
        ]
    else:
        return [
            (y - 1, x),
            (y, x - 1),
            (y, x + 1),
            (y + 1, x),
        ]


low = 0
for y, line in enumerate(heights):
    for x, val in enumerate(line):
        if all([heights[a][b] > val for (a, b) in get_neighbours_coord(x, y, heights)]):
            low += val + 1
print(low)


low_points = {}
visited = {}
for y, line in enumerate(heights):
    for x, val in enumerate(line):
        if all([heights[a][b] > val for (a, b) in get_neighbours_coord(x, y, heights)]):
            low_points[(y, x)] = 0
            visited[(y, x)] = []

for (y, x) in low_points.keys():
    low_points[(y, x)] += 1
    visited[(y, x)].append((y, x))
    neighbours = get_neighbours_coord(x, y, heights)
    while len(neighbours) > 0:
        new_neighbours = []
        for (a, b) in neighbours:
            visited[(y, x)].append((a, b))
            if heights[a][b] != 9:
                low_points[(y, x)] += 1
                ns = get_neighbours_coord(b, a, heights)
                new_neighbours.extend([n for n in ns if n not in visited[(y, x)]])
        neighbours = set(new_neighbours)

res = 1
for i in sorted(low_points.items(), key=lambda x: x[1], reverse=True)[:3]:
    res *= i[1]
print(res)
