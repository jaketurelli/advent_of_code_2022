from collections import deque
MONKIES = []


class Monkey:
    """Monkey class"""

    def __init__(self, number):
        """Init"""
        self.number = number
        self.starting_items = deque()
        self.operation = [0, [0, 0]]
        self.test = None
        self.if_true = None
        self.if_false = None
        self.inspections = 0


if __name__ == "__main__":
    monkey_count = 0
    return_lambda = lambda a: a
    calculate = {'+': lambda a, b: a + b,
                 '-': lambda a, b: a - b,
                 '*': lambda a, b: a * b,
                 '/': lambda a, b: a // b}
    with open("day_11.example.txt", 'r') as file:
        for line in file:
            line = line.replace('\n', '')

            if 'Monkey' in line:
                line_split = line.split(' ')
                MONKIES.append(Monkey(int(line_split[1].strip(':'))))
            if 'Starting items:' in line:
                line_split = line.split(':')[1].split(',')
                for val in line_split:
                    MONKIES[monkey_count].starting_items.append(int(val))
            if 'Operation:' in line:
                line_eval = line.split(':')[1].split('=')[1].strip().split(' ')
                MONKIES[monkey_count].operation[0] = line_eval[1]
                MONKIES[monkey_count].operation[1] = [line_eval[0], line_eval[2]]
                if MONKIES[monkey_count].operation[1][0] == 'old':
                    # MONKIES[monkey_count].operation[1][0] = return_lambda
                    nothin = 1
                else:
                    MONKIES[monkey_count].operation[1][0] = int(MONKIES[monkey_count].operation[1][0])
                if MONKIES[monkey_count].operation[1][1] == 'old':
                    # MONKIES[monkey_count].operation[1][1] = return_lambda
                    nothin = 1
                else:
                    MONKIES[monkey_count].operation[1][1] = int(MONKIES[monkey_count].operation[1][1])

                # MONKIES[monkey_count].operation = line.split(':')[1].split('=')[1].strip()
            if 'Test:' in line:
                MONKIES[monkey_count].test = int(line.split(' ')[-1])
            if 'If true:' in line:
                MONKIES[monkey_count].if_true = int(line.split(' ')[-1])
            if 'If false:' in line:
                MONKIES[monkey_count].if_false = int(line.split(' ')[-1])
                monkey_count = monkey_count + 1

    n_rounds = 1000
    for round in range(1, n_rounds + 1):
        print(f'round: {round}')
        for i, monkey in enumerate(MONKIES):
            n_items = len(monkey.starting_items)
            for j in range(0, n_items):
                old = monkey.starting_items.popleft()
                monkey.inspections = monkey.inspections + 1
                a = 0
                b = 0
                if monkey.operation[1][0] == 'old':
                    a = old
                else:
                    a = monkey.operation[1][0]
                if monkey.operation[1][1] == 'old':
                    b = old
                else:
                    b = monkey.operation[1][1]
                new = calculate[monkey.operation[0]](a, b)
                # new = new // 3
                if new % monkey.test == 0:
                    MONKIES[monkey.if_true].starting_items.append(new)
                else:
                    MONKIES[monkey.if_false].starting_items.append(new)

        # print(f'After round {round}, the monkeys are holding items with these worry levels:')
        # for i, monkey in enumerate(MONKIES):
        #     print(f'Monkey {monkey.number}: ', end='')
        #     for val in monkey.starting_items:
        #         print(f'{val}, ', end='')
        #     print()

    monkey_inspections = []
    for monkey in MONKIES:
        monkey_inspections.append(monkey.inspections)
        print(f'Monkey {monkey.number} inspected items {monkey.inspections} times.')

    sorted_indices = [i[0] for i in sorted(enumerate(monkey_inspections), key=lambda x:x[1])]
    max_monkies = sorted_indices[-2:]
    monkey_business = 1
    for i in max_monkies:
        monkey_business = monkey_business * monkey_inspections[i]
    print(f'monkey business: {monkey_business}')
