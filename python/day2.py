hoz = 0
depth = 0
with open("day2.txt") as f:
    for line in f:
        direction, step = line.strip().split(" ")
        if direction == "forward":
            hoz += int(step)
        elif direction == "down":
            depth += int(step)
        elif direction == "up":
            depth -= int(step)
print(hoz * depth)

hoz = 0
depth = 0
aim = 0
with open("day2.txt") as f:
    for line in f:
        direction, step = line.strip().split(" ")
        if direction == "forward":
            hoz += int(step)
            depth += int(step) * aim
        elif direction == "down":
            aim += int(step)
        elif direction == "up":
            aim -= int(step)

print(hoz * depth)