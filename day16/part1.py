f_map = []
with open('day16/input.txt') as f:
    for line in f:
        f_map.append([*line.strip()])

v_loc = {}
visited = set()
m_height = len(f_map)
m_width = len(f_map[0])

def traverse_maze(loc, dir):
    x = loc[0]
    y = loc[1]
    while(((x, y), dir) not in visited):
        if x < 0 or x >= m_height or y < 0 or y >= m_width:
            return

        if (x, y) not in v_loc:
            v_loc[(x, y)] = 1
        else:
            v_loc[(x, y)] += 1
        visited.add(((x, y), dir))

        p = f_map[x][y]
        if p == '.':
            if dir == 'n':
                x -= 1
            elif dir == 's':
                x += 1
            elif dir == 'e':
                y += 1
            elif dir == 'w':
                y -= 1
        elif p == '/':
            if dir == 'n':
                y += 1
                dir = 'e'
            elif dir == 's':
                y -= 1
                dir = 'w'
            elif dir == 'e':
                x -= 1
                dir = 'n'
            elif dir == 'w':
                x += 1
                dir = 's'
        elif p == '\\':
            if dir == 'n':
                y -= 1
                dir = 'w'
            elif dir == 's':
                y += 1
                dir = 'e'
            elif dir == 'e':
                x += 1
                dir = 's'
            elif dir == 'w':
                x -= 1
                dir = 'n'
        elif p == '|':
            if dir == 'n':
                x -= 1
            elif dir == 's':
                x += 1
            else:
                traverse_maze((x - 1, y), 'n')
                traverse_maze((x + 1, y), 's')
        elif p == '-':
            if dir == 'e':
                y += 1
            elif dir == 'w':
                y -= 1
            else:
                traverse_maze((x, y - 1), 'w')
                traverse_maze((x, y + 1), 'e')


traverse_maze((0, 0), 'e')

print(len(v_loc.values()))
