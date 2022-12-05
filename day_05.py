NUMBER_BINS = 3
NUMBER_BINS = 9
bins = [[], [], [], [], [], [], [], [], [], []]
bin_read_complete = False
with open("day_05.txt", 'r') as file:
    for line in file:
        line = line.replace('\n', '')
        if line == '':
            # print(line)
            x = 1
        elif line[:6] == ' 1   2':
            bin_read_complete = True
            for i in range(1, NUMBER_BINS + 1):
                c_stack = bins[i]
                c_len = len(c_stack)
                new_stack = [0] * c_len
                for j, val in enumerate(c_stack):
                    new_stack[c_len - j - 1] = val
                bins[i] = new_stack
        elif not bin_read_complete:
            for i in range(0, NUMBER_BINS):
                item = line[1 + 4 * i]
                if item != ' ':
                    bins[i + 1].append(line[1 + 4 * i])
        elif line[:4] == 'move':
            line = line.replace("move ", "")
            line = line.replace(" from ", ":")
            line = line.replace(" to ", ":")
            x = line.split(':')
            # print(f'{x[0]} {x[1]} {x[2]}')
            temp = []
            for i in range(int(x[0])):
                popped = bins[int(x[1])].pop()
                temp.append(popped)
            for i in range(int(x[0])):
                popped = temp.pop()
                bins[int(x[2])].append(popped)
            # print(line)
        else:
            # print(line)
            x = 1

final_word = ''
for i in range(1, NUMBER_BINS + 1):
    final_word = final_word + bins[i].pop()
print(final_word)
x = 1
