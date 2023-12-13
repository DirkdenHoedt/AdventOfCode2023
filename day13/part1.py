import itertools
import numpy as np


maps = []
with open('day13/input.txt') as f:
    maps_raw = f.read().split('\n\n')
    for m in maps_raw:
        m = m.split('\n')
        x = []
        for line in m:
            x.append([*line.strip()])
        maps.append(x)

# maps = np.array(maps)
hor_totals = 0
vert_totals = 0

for m in maps:
    m = np.array(m)
    hor_set = set()
    ver_set = set()
    for pair in itertools.combinations(range(len(m)), 2):
        if np.array_equal(m[pair[0]], m[pair[1]]):  # compare columns
            ver_set.add(pair)
    for pair in itertools.combinations(range(len(m[0])), 2):
        if np.array_equal(m[:,pair[0]], m[:,pair[1]]):
            hor_set.add(pair)
    res = []
    if ver_set:
        middle = []
        for p in ver_set:
            if p[0] == p[1] - 1:
                middle.append(p)
        if middle:
            for p in middle:
                min_len = min(p[0] + 1, len(m) - p[1])
                found = True
                for i in range(min_len):
                    if (p[0] - i, p[1] + i) not in ver_set:
                        found = False
                        break
                if found:    
                    res.append((min_len, p[1], False))
    
    if hor_set:
        middle = []
        for p in hor_set:
            if p[0] == p[1] - 1:
                middle.append(p)
        if middle:
            for p in middle:
                min_len = min(p[0] + 1, len(m[0]) - p[1])
                found = True
                for i in range(min_len):
                    if (p[0] - i, p[1] + i) not in hor_set:
                        found = False
                        break
                if found:
                    res.append((min_len, p[1], True))
    if res:
        final = max(res)
        if final[2]:
            hor_totals += final[1]
        else:
            vert_totals += final[1]

print(vert_totals * 100 + hor_totals)
