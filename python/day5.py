points = {}

with open("day5.txt") as f:
    for line in f:
        # print(line)
        start, finish = line.split(" -> ")
        x1, y1 = start.split(",")
        x2, y2 = finish.split(",")
        x1, x2, y1, y2 = int(x1), int(x2), int(y1), int(y2)
        if x1 != x2 and y1 == y2:
            if x1 > x2:
                u, v = x2, x1
            else:
                u, v = x1, x2
            for i in range(u, v + 1):
                p = (i, y1)
                if p in points:
                    points[p] += 1
                else:
                    points[p] = 1
        elif x1 == x2 and y1 != y2:
            if y1 > y2:
                u, v = y2, y1
            else:
                u, v = y1, y2

            for i in range(u, v + 1):
                p = (x1, i)
                if p in points:
                    points[p] += 1
                else:
                    points[p] = 1
print(len([p for p in points.values() if p >= 2]))

# part 2
points = {}

with open("day5.txt") as f:
    for line in f:
        # print(line)
        start, finish = line.split(" -> ")
        x1, y1 = start.split(",")
        x2, y2 = finish.split(",")
        x1, x2, y1, y2 = int(x1), int(x2), int(y1), int(y2)
        if x1 != x2 and y1 == y2:
            if x1 > x2:
                u, v = x2, x1
            else:
                u, v = x1, x2
            for i in range(u, v + 1):
                p = (i, y1)
                if p in points:
                    points[p] += 1
                else:
                    points[p] = 1
        elif x1 == x2 and y1 != y2:
            if y1 > y2:
                u, v = y2, y1
            else:
                u, v = y1, y2

            for i in range(u, v + 1):
                p = (x1, i)
                if p in points:
                    points[p] += 1
                else:
                    points[p] = 1
        elif x1 != x2 and y1 != y2:
            xs = 0
            ys = 0
            if x1 > x2:
                xs = -1
            elif x1 < x2:
                xs = 1
            if y1 > y2:
                ys = -1
            elif y1 < y2:
                ys = 1
            x = x1
            y = y1
            while x != x2 and y != y2:
                p = (x, y)
                if p in points:
                    points[p] += 1
                else:
                    points[p] = 1
                x += xs
                y += ys
            p = (x, y)
            if p in points:
                points[p] += 1
            else:
                points[p] = 1
            x += xs
            y += ys
print(len([p for p in points.values() if p >= 2]))
