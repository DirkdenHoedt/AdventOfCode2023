hands = []

with open('day7/input.txt') as f:
    for line in f:
        line = line.strip().split()
        hands.append((line[0], int(line[1])))

replace_dict = {
    'K': 'B',
    'Q': 'C',
    'J': 'D',
    'T': 'E',
    '9': 'F',
    '8': 'G',
    '7': 'H',
    '6': 'I',
    '5': 'J',
    '4': 'K',
    '3': 'L',
    '2': 'M',
}

def sort_function(x):
    hand = x[0]
    same_chars = [hand.count(e) for e in set(hand)]
    if 5 in same_chars:
        type = 1
    elif 4 in same_chars:
        type = 2
    elif 3 in same_chars and len(same_chars) == 2:
        type = 3
    elif 3 in same_chars:
        type = 4
    elif 2 in same_chars and len(same_chars) == 3:
        type = 5
    elif 2 in same_chars:
        type = 6
    else:
        type = 7
    for s, d in replace_dict.items():
        hand = hand.replace(s, d)
    return type, hand
    
sorted_hands = sorted(hands, key=sort_function)
len_hands = len(sorted_hands)
total = 0
for h in sorted_hands:
    total += h[1] * len_hands
    len_hands -= 1
print(total)