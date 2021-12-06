with open("day6.txt") as f:
    inp = [int(x) for x in f.readline().split(",")]

fish = {x: 0 for x in [0, 1, 2, 3, 4, 5, 6, 7, 8]}
for i in inp:
    fish[i] += 1

for i in range(256):
    if i == 80:
        print(sum(fish.values()))
    new_fish = {x: 0 for x in [0, 1, 2, 3, 4, 5, 6, 7, 8]}
    for ind, x in fish.items():
        if ind == 0:
            new_fish[8] += x
            new_fish[6] += x
        else:
            new_fish[ind - 1] += x
    fish = new_fish

print(sum(fish.values()))
