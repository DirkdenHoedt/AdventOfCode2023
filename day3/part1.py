engine_map = []
result = 0

with open('day3/input.txt') as f:
    for line in f:
        line = line.strip()
        engine_map.append([*line])

length = len(engine_map)
width = len(engine_map[0])
for i, line in enumerate(engine_map):
    number = ''
    special_char_found = False
    for j, char in enumerate(line):
        if char in ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0'):
            number += char
            for x in range(max(i - 1, 0), min(i + 1, length - 1) + 1):
                for y in range(max(j - 1, 0), min(j + 1, width - 1) + 1):
                    if engine_map[x][y] not in ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '.'):
                        special_char_found = True
        else:
            if number != '':
                engine_number = int(number)
                if special_char_found:
                    result += engine_number
                number = ''
                special_char_found = False
    if number != '':
        engine_number = int(number)
        if special_char_found:
            result += engine_number

print(result)