f_map = []
with open('day16/input.txt') as f:
    for line in f:
        f_map.append([*line.strip()])

m_height = len(f_map)
m_width = len(f_map[0])

def traverse_maze(loc, dir, v_loc, visited):
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
                traverse_maze((x - 1, y), 'n', v_loc, visited)
                traverse_maze((x + 1, y), 's', v_loc, visited)
        elif p == '-':
            if dir == 'e':
                y += 1
            elif dir == 'w':
                y -= 1
            else:
                traverse_maze((x, y - 1), 'w', v_loc, visited)
                traverse_maze((x, y + 1), 'e', v_loc, visited)

energized_tiles = []
for i in range(1, m_height - 1):
    v_loc = {}
    visited = set()
    traverse_maze((i, 0), 'e', v_loc, visited)
    energized_tiles.append(len(v_loc.values()))

    v_loc = {}
    visited = set()
    traverse_maze((i, m_width - 1), 'w', v_loc, visited)
    energized_tiles.append(len(v_loc.values()))

for i in range(1, m_width - 1):
    v_loc = {}
    visited = set()
    traverse_maze((0, i), 's', v_loc, visited)
    energized_tiles.append(len(v_loc.values()))

    v_loc = {}
    visited = set()
    traverse_maze((m_height - 1, i), 'n', v_loc, visited)
    energized_tiles.append(len(v_loc.values()))

for i, j, d in [(0, 0, 'e'), (0, 0, 's'), (0, m_width-1, 'w'), (0, m_width-1, 's'), (m_height-1, 0, 'e'), (m_height-1, 0, 'n'), (m_height-1, m_width-1, 'w'), (m_height-1, m_width-1, 'n')]:
    v_loc = {}
    visited = set()
    traverse_maze((i, j), d, v_loc, visited)
    energized_tiles.append(len(v_loc.values()))

print(max(energized_tiles))