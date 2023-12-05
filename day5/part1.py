import re

with open('day5/input.txt') as f:
    sections = f.read().split('\n\n')

seeds = list(map(int, re.findall(r'\d+', sections[0])))

for section in sections[1:]:
    section = section.split('\n')[1:]
    mapper = {}
    for line in section:
        dest, src, lenght = map(int, re.findall(r'\d+', line))
        mapper[(src, src + lenght)] = dest - src
    for i, seed in enumerate(seeds):
        for r in mapper:
            if r[0] <= seed <= r[1]:
                seeds[i] = seed + mapper[r]
                break
print(min(seeds))