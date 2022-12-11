
def get_sync_word(line):
    """ HEre's your doc string
    """
    sync_word = []
    delta = -1
    for i, letter in enumerate(line):
        if letter in sync_word:
            for j, s in enumerate(reversed(sync_word)):
                if s == letter:
                    c_delta = len(sync_word) - j
                    if c_delta > delta:
                        delta = c_delta
                    break

        sync_word.append(letter)
        if len(sync_word) > 14:
            sync_word.pop(0)
            delta = delta - 1

        if delta == 0:
            return i + 1


if __name__ == "__main__":
    with open("day_06.txt", 'r') as file:
        for line in file:
            line = line.replace('\n', '')
            n_char = get_sync_word(line)

    print(f'n_char: {n_char}')
