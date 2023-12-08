from math import lcm
import re


maze = {}

with open('day8/input.txt') as f:
    instructions = [*f.readline().strip()]
    f.readline()
    for line in f:
        m = re.match(r"([A-Z0-9]+) = \(([A-Z0-9]+), ([A-Z0-9]+)\)", line)
        maze[m.group(1)] = (m.group(2), m.group(3))

def solve(current):
    steps = 0
    len_instr = len(instructions)
    while (not current.endswith('Z')):
        instr = instructions[steps % len_instr]
        if instr == 'L':
            current = maze[current][0]
        else:
            current = maze[current][1]
        steps += 1
    return steps

routes = []
for start_point in filter(lambda x: x[-1] == 'A', maze.keys()):
    routes.append(solve(start_point))

print(lcm(*routes))