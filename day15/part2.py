with open('day15/input.txt') as f:
    line = f.readline()
    instr = line.strip().split(',')

def hash_func(input):
    res = 0
    for c in input:
        res += ord(c)
        res *= 17
        res %= 256
    return res

boxes = [{} for _ in range(256)]

for i in instr:
    if '=' in i:
        label, focal = i.split('=')
        boxes[hash_func(label)][label] = int(focal)
    elif '-' in i:
        label = i[:-1]
        try:
            del boxes[hash_func(label)][label]
        except KeyError:
            pass

focus_power = 0
for i, b in enumerate(boxes):
    for j, (k, v) in enumerate(b.items()):
        focus_power += (i + 1) * (j + 1) * v

print(focus_power)