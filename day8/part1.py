import re


maze = {}

with open('day8/input.txt') as f:
    instructions = [*f.readline().strip()]
    f.readline()
    for line in f:
        m = re.match(r"([A-Z]+) = \(([A-Z]+), ([A-Z]+)\)", line)
        maze[m.group(1)] = (m.group(2), m.group(3))

current = 'AAA'
steps = 0
len_instr = len(instructions)
while (current != 'ZZZ'):
    instr = instructions[steps % len_instr]
    if instr == 'L':
        current = maze[current][0]
    else:
        current = maze[current][1]
    steps += 1

print(steps)