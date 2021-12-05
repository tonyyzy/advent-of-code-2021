def parse_board(x):
    return [[int(x) for x in l.split()] for l in x.split("\n")]


# all elements in boards are unique
def ind_num(b, n):
    for i, line in enumerate(b):
        for j, el in enumerate(line):
            if el == n:
                return (i, j)


with open("day4.txt") as f:
    nums = [int(x) for x in f.readline().split(",")]
    rest = f.read()


boards = [parse_board(b) for b in rest.lstrip().split("\n\n")]

score = {x: {} for x in range(len(boards))}

marked = {x: [] for x in range(len(boards))}

for n in nums:
    for (ind, b) in enumerate(boards):
        if (loc := ind_num(b, n)) != None:
            marked[ind].append(n)
            if f"{loc[0]}r" in score[ind].keys():
                score[ind][f"{loc[0]}r"] += 1
                if score[ind][f"{loc[0]}r"] == 5:
                    print((sum([sum(x) for x in b]) - sum(marked[ind])) * n)
                    break
            else:
                score[ind][f"{loc[0]}r"] = 1
            if f"{loc[1]}c" in score[ind].keys():
                score[ind][f"{loc[1]}c"] += 1
                if score[ind][f"{loc[1]}c"] == 5:
                    print((sum([sum(x) for x in b]) - sum(marked[ind])) * n)
                    break
            else:
                score[ind][f"{loc[1]}c"] = 1
    else:
        continue
    break


with open("day4.txt") as f:
    nums = [int(x) for x in f.readline().split(",")]
    rest = f.read()


boards = {ind: parse_board(b) for ind, b in enumerate(rest.lstrip().split("\n\n"))}

score = {x: {} for x in range(len(boards))}

marked = {x: [] for x in range(len(boards))}


for n in nums:
    for ind in list(boards.keys()):
        if ind in boards.keys():
            b = boards[ind]
            if (loc := ind_num(b, n)) != None:
                marked[ind].append(n)
                if f"{loc[0]}r" in score[ind].keys():
                    score[ind][f"{loc[0]}r"] += 1
                    if score[ind][f"{loc[0]}r"] == 5:
                        if len(boards) == 1:
                            print((sum([sum(x) for x in b]) - sum(marked[ind])) * n)
                            exit()
                        else:
                            boards.pop(ind)
                            continue
                else:
                    score[ind][f"{loc[0]}r"] = 1
                if f"{loc[1]}c" in score[ind].keys():
                    score[ind][f"{loc[1]}c"] += 1
                    if score[ind][f"{loc[1]}c"] == 5:
                        if len(boards) == 1:
                            print((sum([sum(x) for x in b]) - sum(marked[ind])) * n)
                            exit()
                        else:
                            boards.pop(ind)
                else:
                    score[ind][f"{loc[1]}c"] = 1
