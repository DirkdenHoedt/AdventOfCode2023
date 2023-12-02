games = {}
with open('day2/input.txt') as f:
    for i, line in enumerate(f):
        games[i + 1] = {'red': 0, 'green': 0, 'blue': 0}
        line = line.strip()
        game_info = line.split(':')[1]
        subsets = game_info.split(';')
        for subset in subsets:
            turns = subset.split(',')
            for turn in turns:
                turn = turn.strip()
                amount, color = turn.split(' ')
                games[i + 1][color] = max(games[i + 1][color], int(amount))

total = 0
for _, game in games.items():
    total += game['red'] * game['green'] * game['blue']

print(f"Answer: {total}")