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

total = 0
for i in instr:
    res = hash_func(i)
    total += res

print(total)