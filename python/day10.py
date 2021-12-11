line = "{([(<{}[<>[]}>{[]{[(<()>"

with open("day10.txt") as f:
    lines = [x.strip() for x in f.readlines()]

cost = {")": 3, "]": 57, "}": 1197, ">": 25137}


def cursed(inp):
    s = ""
    for i in inp:
        if i in "{[<(":
            s += i
        elif i == "}":
            if s[-1] == "{":
                s = s[:-1]
            else:
                return False, i
        elif i == ")":
            if s[-1] == "(":
                s = s[:-1]
            else:
                return False, i
        elif i == "]":
            if s[-1] == "[":
                s = s[:-1]
            else:
                return False, i
        elif i == ">":
            if s[-1] == "<":
                s = s[:-1]
            else:
                return False, i
    return True, s


total = 0
for line in lines:
    a, b = cursed(line)
    if not a:
        total += cost[b]
print(total)


scores = []
for line in lines:
    a, b = cursed(line)
    if a:
        total = 0
        while b != "":
            if b[-1] == "(":
                total *= 5
                total += 1
                b = b[:-1]
            elif b[-1] == "[":
                total *= 5
                total += 2
                b = b[:-1]
            elif b[-1] == "{":
                total *= 5
                total += 3
                b = b[:-1]
            elif b[-1] == "<":
                total *= 5
                total += 4
                b = b[:-1]
        scores.append(total)

i = int(len(scores) / 2)
print(sorted(scores)[i])
