nums = []
with open("day1.txt") as f:
    for line in f:
        nums.append(int(line))
counter = 0
for idx in range(1, len(nums)):
    if nums[idx] > nums[idx - 1]:
        counter += 1
print(counter)

sums = []
for idx in range(2, len(nums)):
    sums.append(sum(nums[idx - 2 : idx + 1]))

counter = 0
for idx in range(1, len(sums)):
    if sums[idx] > sums[idx - 1]:
        counter += 1
print(counter)
