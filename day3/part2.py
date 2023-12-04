engine_map = []
gears = {}
result = 0

with open('day3/input.txt') as f:
    for line in f:
        line = line.strip()
        engine_map.append([*line])

length = len(engine_map)
width = len(engine_map[0])
for i, line in enumerate(engine_map):
    number = ''
    gear_locations = set()
    for j, char in enumerate(line):
        if char in ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0'):
            number += char
            for x in range(max(i - 1, 0), min(i + 1, length - 1) + 1):
                for y in range(max(j - 1, 0), min(j + 1, width - 1) + 1):
                    if engine_map[x][y] == '*':
                        gear_locations.add((x, y))
        else:
            if number != '':
                engine_number = int(number)
                for gear_location in gear_locations:
                    if gear_location in gears:
                        gears[gear_location].append(engine_number)
                    else:
                        gears[gear_location] = [engine_number]
                number = ''
                gear_locations = set()
    if number != '':
        engine_number = int(number)
        for gear_location in gear_locations:
            if gear_location in gears:
                gears[gear_location].append(engine_number)
            else:
                gears[gear_location] = [engine_number]

for gear_loc in gears:
    if len(gears[gear_loc]) == 2:
        result += gears[gear_loc][0] * gears[gear_loc][1]

print(result)