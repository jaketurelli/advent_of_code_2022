X = []
X.append(1)
# X.append(1)
OUTPUT = []
OUTPUT.append(1)
# OUTPUT.append(1)


def update_output(_index):
    """updtate output"""
    global X, OUTPUT
    OUTPUT.append(0)
    index = (_index) % 40
    if X[_index] - 1 <= index and X[_index] + 1 >= index:
        OUTPUT[_index] = 1


if __name__ == "__main__":

    with open("day_10.txt", 'r') as file:

        index = 0
        for line in file:
            line = line.replace('\n', '')
            line = line.split(' ')
            if line[0] == 'noop':
                X.append(X[index])
                update_output(index)
                index = index + 1

            else:

                X.append(X[index])
                update_output(index)
                index = index + 1
                X.append(X[index - 1] + int(line[1]))
                update_output(index)
                index = index + 1

    cycles = [20, 60, 100, 140, 180, 220]
    strength = 0
    for cycle in cycles:
        strength = strength + cycle * X[cycle]
        print(f'cycle: {cycle * X[cycle]}')

    print(f'total strength: {strength}')

    for i, val in enumerate(OUTPUT):
        if val == 1:
            print('#', end='')
        else:
            print('.', end='')
        if (i + 1) % 40 == 0:
            print()
