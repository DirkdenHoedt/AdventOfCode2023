field = []

with open('day14/input.txt') as f:
    for line in f:
        field.append([*line.strip()])

def print_field():
    for line in field:
        print(''.join(line))
    input()

for i, line in enumerate(field):
    for j, el in enumerate(line):
        if el == 'O':
            next_y = max(-1, i - 1)
            while field[next_y][j] != 'O' and field[next_y][j] != '#' and next_y >= 0:
                next_y = max(-1, next_y - 1)
            field[i][j] = '.'
            field[next_y + 1][j] = 'O'

len_field = len(field)
total = 0
for i, line in enumerate(field):
    for el in line:
        if el == 'O':
            total += len_field - i

print(total)
