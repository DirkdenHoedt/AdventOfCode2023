import re

with open('day5/input.txt') as f:
    sections = f.read().split('\n\n')

seed_ranges = list(map(int, re.findall(r'\d+', sections[0])))
seeds = []
for i in range(0, len(seed_ranges), 2):
    seeds.append((seed_ranges[i], seed_ranges[i] + seed_ranges[i+1] - 1))

for section in sections[1:]:
    section = section.split('\n')[1:]
    mapper = {}
    for line in section:
        dest, src, lenght = map(int, re.findall(r'\d+', line))
        mapper[(src, src + lenght - 1)] = dest - src
    new_seeds = []
    for start, end in seeds:
        covered_ranges = []
        for r in mapper:
            if end < r[0] or start > r[1]:
                continue
            # if r[0] <= start <= r[1] or r[0] <= end <= r[1]:
            range_start = max(r[0], start)
            range_end = min(r[1], end)
            new_seeds.append((range_start + mapper[r], range_end + mapper[r]))
            covered_ranges.append((range_start, range_end))
        if not covered_ranges:
            new_seeds.append((start, end))
            continue
        covered_ranges.sort()
        if covered_ranges[0][0] > start:
            new_seeds.append((start, covered_ranges[0][0] - 1))
        if covered_ranges[-1][1] < end:
            new_seeds.append((covered_ranges[-1][1] + 1, end))
        for i in range(len(covered_ranges) - 1):
            a, b = covered_ranges[i]
            c, d = covered_ranges[i+1]
            if c > b + 1:
                new_seeds.append((b + 1, c - 1))
    seeds = new_seeds

print(min(seeds)[0])