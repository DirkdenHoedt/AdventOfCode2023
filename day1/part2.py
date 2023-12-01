import re

def conv_to_number(num):
    if num == 'one':
        return '1'
    elif num == 'two':
        return '2'
    elif num == 'three':
        return '3'
    elif num == 'four':
        return '4'
    elif num == 'five':
        return '5'
    elif num == 'six':
        return '6'
    elif num == 'seven':
        return '7'
    elif num == 'eight':
        return '8'
    elif num == 'nine':
        return '9'

result = 0
with open('day1/input.txt') as f:
    for line in f:
        line = line.strip()
        digits = re.findall(r'(?=(\d|one|two|three|four|five|six|seven|eight|nine))', line)
        first = digits[0]
        last = digits[-1]
        if len(first) != 1:
            first = conv_to_number(first)
        if len(last) != 1:
            last = conv_to_number(last)
        outcome = int(first + last)
        print(outcome)
        result += outcome
print(result)