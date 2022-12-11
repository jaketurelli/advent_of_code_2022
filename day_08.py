
# todo: need to capture a "max" tree line value instead of prior tree.
FOREST = []
VISIBLE_TREE_MATRIX = []


def get_up(x, y):
    """get up score"""
    score = 1
    ind = y - 1
    while ind > 0:
        if FOREST[x][ind] < FOREST[x][y]:
            score = score + 1
        else:
            return score
        ind = ind - 1
    return score


def get_down(x, y):
    """get down score"""
    score = 1
    for i in range(y + 1, n_rows - 1):
        if FOREST[x][i] < FOREST[x][y]:
            score = score + 1
        else:
            return score
    return score


def get_left(x, y):
    """get left score"""
    score = 1
    ind = x - 1
    while ind > 0:
        if FOREST[ind][y] < FOREST[x][y]:
            score = score + 1
        else:
            return score
        ind = ind - 1
    return score


def get_right(x, y):
    """get right score"""
    score = 1
    for i in range(x + 1, n_cols - 1):
        if FOREST[i][y] < FOREST[x][y]:
            score = score + 1
        else:
            return score
    return score


def get_score(x, y):
    """get score"""
    a = get_up(x, y)
    b = get_down(x, y)
    c = get_left(x, y)
    d = get_right(x, y)
    return a * b * c * d


def find_visibility_up_down(direction):
    """find visibility"""
    global VISIBLE_TREE_MATRIX
    global FOREST

    for col in range(1, n_cols - 1):
        col_ind = col
        if direction == 'up':
            max_val = FOREST[n_rows - 1][col]
        else:
            max_val = FOREST[0][col]
        for row in range(1, n_rows - 1):
            row_ind = row
            if direction == 'up':
                row_ind = n_rows - row - 1

            if FOREST[row_ind][col_ind] > max_val:
                VISIBLE_TREE_MATRIX[row_ind][col_ind] = 1
                max_val = FOREST[row_ind][col_ind]
            # else:
            #     print(f'not visible at {col_ind} x {row_ind}')


def find_visibility_left_right(direction):
    """find visibility"""
    global VISIBLE_TREE_MATRIX
    global FOREST

    for row in range(1, n_rows - 1):
        row_ind = row
        if direction == 'right to left':
            max_val = FOREST[row][n_cols - 1]
        if direction == 'left to right':
            max_val = FOREST[row][0]
        for col in range(1, n_cols - 1):
            col_ind = col
            if direction == 'right to left':
                col_ind = n_cols - col - 1
            if FOREST[row_ind][col_ind] > max_val:
                VISIBLE_TREE_MATRIX[row_ind][col_ind] = 1
                max_val = FOREST[row_ind][col_ind]
            # else:
                # print(f'not visible at {col_ind} x {row_ind}')


if __name__ == "__main__":
    # global VISIBLE_TREE_MATRIX
    # global FOREST

    with open("day_08.txt", 'r') as file:
        n_rows = 0
        for line in file:
            row = []
            line = line.replace('\n', '')
            n_cols = len(line)
            n_rows = n_rows + 1
            for val in line:
                row.append(int(val))

            FOREST.append(row)

    print(f'matrix is {n_rows} x {n_cols}')
    # VISIBLE_TREE_MATRIX = n_rows * [n_cols * [0]]
    VISIBLE_TREE_MATRIX = [[0] * n_cols for _ in range(n_rows)]

    # left to right
    find_visibility_left_right('left to right')

    # right to left
    find_visibility_left_right('right to left')

    # top down
    find_visibility_up_down('down')

    # down up
    find_visibility_up_down('up')

    visible_trees = n_cols * 2 + (n_rows - 2) * 2
    for row in range(1, n_rows - 1):
        for col in range(1, n_cols - 1):
            visible_trees = visible_trees + VISIBLE_TREE_MATRIX[row][col]

    max_visibility_score = 0
    for row in range(1, n_rows - 1):
        for col in range(1, n_cols - 1):
            visibility_score = get_score(row, col)
            if visibility_score > max_visibility_score:
                max_visibility_score = visibility_score

    print(f'visible trees: {visible_trees}')
    print(f'max visibility: {max_visibility_score}')
