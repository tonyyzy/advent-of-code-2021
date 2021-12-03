import numpy as np

arr = []
gamma = 0b0
epsilon = 0b0
l = 0

with open("day3.txt") as f:
    for line in f:
        l += 1
        arr.append([x == "1" for x in line.strip()])

arr = np.array(arr)

for i in arr.sum(axis=0) > l / 2:
    gamma <<= 1
    epsilon <<= 1
    if i:
        gamma += 0b1
    else:
        epsilon += 0b1
print(gamma * epsilon)


def pack(arr):
    x = 0b0
    for i in arr:
        x <<= 1
        if i:
            x += 0b1
    return x


o2 = arr.copy()
co2 = arr.copy()

o2b = 0
co2b = 0

while o2.shape[0] > 1 and o2b < o2.shape[1]:
    b = o2[:, o2b].sum() >= o2.shape[0] / 2
    o2 = o2[o2[:, o2b] == b]
    o2b += 1

while co2.shape[0] > 1 and co2b < co2.shape[1]:
    b = co2[:, co2b].sum() < co2.shape[0] / 2
    co2 = co2[co2[:, co2b] == b]
    co2b += 1
print(pack(o2[0]) * pack(co2[0]))
