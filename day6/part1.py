with open('day6/input.txt') as f:
    time = map(int, f.readline().strip().split(':')[1].split())
    distance = map(int, f.readline().strip().split(':')[1].split())

result = 1
for t, d in zip(time, distance):
    win = 0
    for i in range(t + 1):
        dist = i * (t - i)
        if dist > d:
            win += 1
    result *= win

print(result)
