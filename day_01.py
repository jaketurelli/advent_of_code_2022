import numpy as np

elf_calories = [0]
elf_index = 0
elf_calories[elf_index] = 0
with open("day_01.txt", 'r') as file:
    for line in file:
        if line == '\n':
            elf_index = elf_index + 1
            elf_calories.append(0)
            # print(f"elf cal count: {elf_calories[elf_index-1]}")
        else:
            elf_calories[elf_index] = elf_calories[elf_index] + int(line)

max_elf_index = 0
max_cals = elf_calories[max_elf_index]
for elf, cals in enumerate(elf_calories):
    print(f"elf {elf+1} had {cals} cals")
    if cals > max_cals:
        max_elf_index = elf
        max_cals = cals

print(f'elf {max_elf_index+1} had most cals of {max_cals}')


# sorted_list = numpy.argsort((-elf_calories))
np_list = np.array(elf_calories)
sorted_list = np_list.argsort()[::-1][:3]
total_cals = 0
for i in range(0, 3):
    total_cals = total_cals + elf_calories[sorted_list[i]]
    print(f'calories {elf_calories[sorted_list[i]]} ')

print(f'total cals: {total_cals}')
