KNOT = [[0, 0],
        [0, 0],
        [0, 0],
        [0, 0],
        [0, 0],
        [0, 0],
        [0, 0],
        [0, 0],
        [0, 0],
        [0, 0]
        ]

HX = 0
HY = 0
TX = 0
TY = 0
TAIL_SPACES = {}
TAIL_SPACES_KNOT = {}
TAIL_SPACES[tuple([0, 0])] = 1
TAIL_SPACES_KNOT[tuple([0, 0])] = 1


def is_move_needed():
    """is move needed"""
    return abs(HX - TX) > 1 or abs(HY - TY) > 1


def is_move_needed_knot(move_index):
    """is move needed"""
    return abs(KNOT[move_index - 1][0] - KNOT[move_index][0]) > 1 or abs(KNOT[move_index - 1][1] - KNOT[move_index][1]) > 1


def move_knot(direction, value):
    """move right"""
    global KNOT, TAIL_SPACES_KNOT

    for ind in range(0, value):
        if direction == 'R':
            KNOT[0][0] = KNOT[0][0] + 1
        elif direction == 'L':
            KNOT[0][0] = KNOT[0][0] - 1
        elif direction == 'U':
            KNOT[0][1] = KNOT[0][1] + 1
        elif direction == 'D':
            KNOT[0][1] = KNOT[0][1] - 1
        for i in range(1, len(KNOT)):

            if not is_move_needed_knot(i):
                continue

            deltax = KNOT[i - 1][0] - KNOT[i][0]
            deltay = KNOT[i - 1][1] - KNOT[i][1]
            if abs(deltax) > 0:
                KNOT[i][0] = KNOT[i][0] + deltax // abs(deltax)
            if abs(deltay) > 0:
                KNOT[i][1] = KNOT[i][1] + deltay // abs(deltay)

            TAIL_SPACES_KNOT[tuple([KNOT[9][0], KNOT[9][1]])] = 1


def move(direction, value):
    """move right"""
    global HX, HY, TX, TY, TAIL_SPACES

    for ind in range(0, value):

        if direction == 'R':
            HX = HX + 1
        elif direction == 'L':
            HX = HX - 1
        elif direction == 'U':
            HY = HY + 1
        elif direction == 'D':
            HY = HY - 1

        if not is_move_needed():
            continue

        deltax = HX - TX
        deltay = HY - TY
        if abs(deltax) > 0:
            TX = TX + deltax // abs(deltax)
        if abs(deltay) > 0:
            TY = TY + deltay // abs(deltay)

        TAIL_SPACES[tuple([TX, TY])] = 1


if __name__ == "__main__":

    with open("day_09.txt", 'r') as file:
        for line in file:
            line = line.replace('\n', '')
            line = line.split(' ')

            # move(line[0], int(line[1]))
            move_knot(line[0], int(line[1]))

    # print(f'number tail spaces: {len(TAIL_SPACES)}')
    print(f'number tail spaces: {len(TAIL_SPACES_KNOT)}')
