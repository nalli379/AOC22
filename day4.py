import re
import numpy as np



def create_arr(string):
    start = int(string[0])
    stop= int(string[-1]) + 1

    arr = set(np.arange(start, stop))
    
    return arr


count = 0

with open('day4_input.txt', 'r') as f:
    lines = f.readlines()

    for line in lines:
        line = re.sub('\n', '', line)
        elf1, elf2 = line.split(',')
        elf1 = elf1.split('-')
        elf2 = elf2.split('-')

        elf1 = create_arr(elf1)
        elf2 = create_arr(elf2)

        if len(elf1.intersection(elf2)) > 0:
            count += 1
    

    print(count)

    

        





        

