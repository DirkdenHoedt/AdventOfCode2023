seqs = []

with open('day9/input.txt') as f:
    for line in f:
        seqs.append(list(map(int, line.strip().split())))

def solve(seq):
    iterations = [seq]
    while(min(iterations[-1]) != 0 or max(iterations[-1]) != 0):
        it = []
        for i in range(len(iterations[-1]) - 1):
            it.append(iterations[-1][i + 1] - iterations[-1][i])
        iterations.append(it)
    res = 0
    for it in iterations:
        res += it[-1]
    return res
        

result = 0
for seq in seqs:
    result += solve(seq)

print(result)
