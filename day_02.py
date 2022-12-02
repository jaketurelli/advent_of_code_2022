
# A: Rock
# B: Paper
# C: Scissors

# X: Rock - 1
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


win = {
    'A': 'Y',
    'B': 'Z',
    'C': 'X'
}

lose = {
    'A': 'Z',
    'B': 'X',
    'C': 'Y'
}

tie = {
    'A': 'X',
    'B': 'Y',
    'C': 'Z'
}

part2_score = {
    'X': 0,
    'Y': 3,
    'Z': 6
}

total_score = 0
total_score2 = 0
with open("day_02.txt", 'r') as file:
    for line in file:
        line = line.replace('\n', '')
        hands = line.split(' ')
        # score of hand 1
        hand_score = my_points[hands[1]]
        win_score = hand_scores[hands[0] + hands[1]]
        total_score = total_score + hand_score + win_score

        # PART 2
        win_score2 = part2_score[hands[1]]
        if(hands[1] == 'X'):
            hand_score2 = my_points[lose[hands[0]]]
        if(hands[1] == 'Y'):
            hand_score2 = my_points[tie[hands[0]]]
        if(hands[1] == 'Z'):
            hand_score2 = my_points[win[hands[0]]]
        total_score2 = total_score2 + hand_score2 + win_score2


print(f'total score: {total_score}')
print(f'total score2: {total_score2}')
