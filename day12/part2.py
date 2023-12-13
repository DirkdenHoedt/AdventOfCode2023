import functools


data = []
with open('day12/input.txt') as f:
    for line in f:
        a, b = line.strip().split()
        b = tuple(map(int, b.split(',')))
        data.append(('?'.join([a] * 5), b * 5))

@functools.cache
def solve(x1: str, x2: list, runtime=0):
    if not x1:
        if (len(x2) == 0 and runtime == 0) or (len(x2) == 1 and x2[0] == runtime):
            return 1
        return 0
    x = x1[0]
    x1 = x1[1:]
    y, *y2 = x2 or [0]
    y2 = tuple(y2)
    
    if x == '?':
        return solve('#' + x1, x2, runtime) + solve('.' + x1, x2, runtime)
    elif x == '#':
        if runtime > y:
            return 0
        return solve(x1, x2, runtime + 1)
    elif x == '.':
        if runtime == 0:
            return solve(x1, x2, 0)
        if runtime == y:
            return solve(x1, y2, 0)
        return 0

result = 0
for d in data:
    test = solve(d[0], d[1])
    # print(test)
    result += test
print(result)