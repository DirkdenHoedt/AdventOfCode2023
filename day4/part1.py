total_score = 0
with open('day4/input.txt') as f:
    for line in f:
        line = line.strip()
        raw = line.split(':')[1].split('|')
        win_numbers = set(map(int, raw[0].strip().split()))
        all_numbers = set(map(int, raw[1].strip().split()))
        correct_count = len(win_numbers.intersection(all_numbers))
        score = 0
        for i in range(correct_count):
            if i == 0:
                score = 1
            else:
                score *= 2
        total_score += score
print(total_score)