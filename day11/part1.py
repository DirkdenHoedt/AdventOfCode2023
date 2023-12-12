gals = []
with open('day11/input.txt') as f:
    for y,r in enumerate(f):
        for x,c in enumerate(r):
            if c == '#':
                gals.append((x, y))

xs, ys = zip(*gals)
    
def solve(ps):
    ps = [sum((2, 1)[p in ps] for p in range(p)) for p in ps]
    return sum(abs(a-b) for a in ps for b in ps)//2

result = solve(xs)
result += solve(ys)
print(result)