with open('day6/input.txt') as f:
    time = [int(f.readline().strip().split(':')[1].replace(" ", ""))]
    distance = [int(f.readline().strip().split(':')[1].replace(" ", ""))]

result = 1
for t, d in zip(time, distance):
    win = 0
    for i in range(t + 1):
        dist = i * (t - i)
        if dist > d:
            win += 1
    result *= win

print(result)