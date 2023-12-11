maze = []

with open('day10/input.txt') as f:
    for line in f:
        maze.append([*line.strip()])

start_pos = (-1, -1)
for i, x in enumerate(maze):
    for j, y in enumerate(x):
        if y == 'S':
            start_pos = (i, j)
            break
    if start_pos != (-1, -1):
        break

route = [start_pos]
current_pos = None
if maze[start_pos[0] - 1][start_pos[1]] in ('|', '7', 'F'):
    route.append((start_pos[0] - 1, start_pos[1]))
    current_pos = maze[start_pos[0] - 1][start_pos[1]]
elif maze[start_pos[0] + 1][start_pos[1]] in ('|', 'L', 'J'):
    route.append((start_pos[0] + 1, start_pos[1]))
    current_pos = maze[start_pos[0] + 1][start_pos[1]]
elif maze[start_pos[0]][start_pos[1] - 1] in ('-', 'L', 'F'):
    route.append((start_pos[0] + 1, start_pos[1]))
    current_pos = maze[start_pos[0]][start_pos[1] - 1]
elif maze[start_pos[0]][start_pos[1] + 1] in ('-', '7', 'J'):
    route.append((start_pos[0] + 1, start_pos[1]))
    current_pos = maze[start_pos[0]][start_pos[1] + 1]

while(current_pos != 'S'):
    if current_pos == '-':
        new_x = route[-1][0]
        new_y = route[-1][1] + 1 if route[-1][1] > route[-2][1] else route[-1][1] - 1
        route.append((new_x, new_y))
        current_pos = maze[new_x][new_y]
    elif current_pos == 'L':
        if route[-2][0] < route[-1][0]:
            new_x = route[-1][0]
            new_y = route[-1][1] + 1
        else:
            new_x = route[-1][0] - 1
            new_y = route[-1][1]
        route.append((new_x, new_y))
        current_pos = maze[new_x][new_y]
    elif current_pos == 'F':
        if route[-2][0] > route[-1][0]:
            new_x = route[-1][0]
            new_y = route[-1][1] + 1
        else:
            new_x = route[-1][0] + 1
            new_y = route[-1][1]
        route.append((new_x, new_y))
        current_pos = maze[new_x][new_y]
    elif current_pos == '|':
        new_x = route[-1][0] + 1 if route[-1][0] > route[-2][0] else route[-1][0] - 1
        new_y = route[-1][1]
        route.append((new_x, new_y))
        current_pos = maze[new_x][new_y]
    elif current_pos == '7':
        if route[-2][0] > route[-1][0]:
            new_x = route[-1][0]
            new_y = route[-1][1] - 1
        else:
            new_x = route[-1][0] + 1
            new_y = route[-1][1]
        route.append((new_x, new_y))
        current_pos = maze[new_x][new_y]
    elif current_pos == 'J':
        if route[-2][0] < route[-1][0]:
            new_x = route[-1][0]
            new_y = route[-1][1] - 1
        else:
            new_x = route[-1][0] - 1
            new_y = route[-1][1]
        route.append((new_x, new_y))
        current_pos = maze[new_x][new_y]

print(int(len(route[:-1]) / 2))