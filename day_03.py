
print(ord('r') - 97 + 1)
print(ord('Z') - 65 + 27)

with open("day_03.txt", 'r') as file:
    total_priority = 0
    total_badge_priority = 0
    line_num = 1
    lines = []
    for line in file:
        line = line.replace('\n', '')
        lines.append(line)
        if line_num > 3:
            lines.pop(0)

        if line_num % 3 == 0:

            common_badge = {}
            for i in lines[0]:
                common_badge[i] = 1
            common_badge_2 = {}
            for j in lines[1]:
                if j in common_badge:
                    common_badge_2[j] = 1
            for k in lines[2]:
                if k in common_badge_2:
                    shared_badge = k

            if shared_badge.islower():
                shared_badge_value = ord(shared_badge) - 97 + 1
            else:
                shared_badge_value = ord(shared_badge) - 65 + 27
            total_badge_priority = total_badge_priority + shared_badge_value
            # print(f'badge: {shared_badge} - {shared_badge_value}')

        size = len(line)
        part1 = line[:size // 2]
        part2 = line[size // 2:]
        common_dict = {}
        for i in part1:
            common_dict[i] = 1
        for j in part2:
            if j in common_dict:
                shared = j
        curr_priority = 0
        if shared.islower():
            curr_priority = ord(shared) - 97 + 1
        else:
            curr_priority = ord(shared) - 65 + 27
        total_priority = total_priority + curr_priority
        line_num = line_num + 1
        # print(f'{line}({shared} - {curr_priority})')

print(f'total priority: {total_priority}')
print(f'total_badge_priority: {total_badge_priority}')
