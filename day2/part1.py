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
valid_games = []
for game_id, game in games.items():
    if game['red'] <= 12 and game['green'] <= 13 and game['blue'] <= 14:
        total += game_id
        valid_games.append(game_id)

print(f"Answer: {total}")
print(f"Valid game IDs: {valid_games}")