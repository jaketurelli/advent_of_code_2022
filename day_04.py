
total_fully_contain = 0
total_separate = 0
total = 0
with open("day_04.txt", 'r') as file:
    for line in file:
        line = line.replace('\n', '')
        a = line.split(',')
        minmax1 = a[0].split('-')
        minmax2 = a[1].split('-')
        if ((int(minmax1[0]) <= int(minmax2[0])) and (int(minmax1[1]) >= int(minmax2[1]))) or \
           ((int(minmax2[0]) <= int(minmax1[0])) and (int(minmax2[1]) >= int(minmax1[1]))):
            total_fully_contain = total_fully_contain + 1
        if ((int(minmax1[1]) < int(minmax2[0])) or (int(minmax1[0]) > int(minmax2[1]))):
            total_separate = total_separate + 1
            print(line)
        total = total + 1

print(f'total_fully_contain: {total_fully_contain}')
print(f'total_partial_contain: {total-total_separate}')
