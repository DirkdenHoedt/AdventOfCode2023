total_score = 0
cards = []
card_copies = []
with open('day4/input.txt') as f:
    for line in f:
        line = line.strip()
        raw = line.split(':')[1].split('|')
        win_numbers = set(map(int, raw[0].strip().split()))
        all_numbers = set(map(int, raw[1].strip().split()))
        
        correct_count = len(win_numbers.intersection(all_numbers))
        cards.append(correct_count)
        card_copies.append(1)

for i, correct in enumerate(cards):
    for j in range(i + 1, i + 1 + correct):
        card_copies[j] += card_copies[i]

print(sum(card_copies))