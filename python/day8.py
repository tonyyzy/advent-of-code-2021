from collections import Counter

counter = 0
with open("day8.txt") as f:
    for line in f.readlines():
        digits, nums = line.split(" | ")
        for num in nums.split():
            if len(num) in [2, 4, 3, 7]:
                counter += 1
print(counter)

disp = [
    "abcefg",
    "cf",
    "acdeg",
    "acdfg",
    "bcdf",
    "abdfg",
    "abdefg",
    "acf",
    "abcdefg",
    "abcdfg",
]

mapper = {}
for i, n in enumerate(disp):
    mapper["".join(sorted(n))] = str(i)


def decode(digits, nums):
    letters = {x: [] for x in range(2, 8)}
    for i in digits.split():
        letters[len(i)].append(i)
    a = [x for x in letters[3][0] if x not in letters[2][0]][0]
    bd = [x for x in letters[4][0] if x not in letters[2][0]]
    six = Counter([y for x in letters[6] for y in x])
    cde = [x for x, y in six.items() if y < 3]
    c = [x for x in cde if x in letters[2][0]][0]
    f = [x for x in letters[2][0] if x not in c][0]
    de = [x for x in cde if x not in c]
    d = [x for x in de if x in letters[4][0]][0]
    e = [x for x in de if x not in d][0]
    b = [x for x in bd if x not in d][0]
    g = [x for x in "abcdefg" if x not in [a, b, c, d, e, f]][0]

    dec = {
        a: "a",
        b: "b",
        c: "c",
        d: "d",
        e: "e",
        f: "f",
        g: "g",
    }
    num = ""
    for n in nums.split():
        num += mapper["".join(sorted([dec[x] for x in n]))]
    return int(num)


total = 0
with open("day8.txt") as f:
    for line in f.readlines():
        digits, nums = line.split(" | ")
        total += decode(digits, nums)
print(total)
