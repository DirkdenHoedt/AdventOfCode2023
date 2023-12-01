import re

result = 0
with open('day1/input.txt') as f:
    for line in f:
        digits = re.findall(r'\d', line)
        result += int(digits[0] + digits[-1])
print(result)