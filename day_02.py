
# A: Rock
# B: Paper
# C: Scissors

# Z: Rock - 1
# Y: Paper - 2
# Z: Scissors - 3

# 0 loss
# 3 tie
# 6 win

their_points = {'A': 1,
                'B': 2,
                'C': 3}
my_points = {'X': 1,
             'Y': 2,
             'Z': 3}

hand_scores = {
    'AX': 3,
    'AY': 6,
    'AZ': 0,

    'BX': 0,
    'BY': 3,
    'BZ': 6,

    'CX': 6,
    'CY': 0,
    'CZ': 3}


total_score = 0
with open("day_02.txt", 'r') as file:
    for line in file:
        line = line.replace('\n', '')
        hands = line.split(' ')
        # score of hand
        hand_score = my_points[hands[1]]
        win_score = hand_scores[hands[0] + hands[1]]
        total_score = total_score + hand_score + win_score

        print(f'{hands[0]} {hands[1]}')

print(f'total score: {total_score}')
