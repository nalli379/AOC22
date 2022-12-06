from iteration_utilities import duplicates
import string
import re

#create dictionary for all lower/uppercase letters and the priority
allAlphabet = string.ascii_letters
allAlphaValues = {}

count = 1
for letter in range(len(allAlphabet)):
    allAlphaValues[allAlphabet[letter]] = count
    count += 1



#create dictionary for all rucksacks and all duplicates
groupDup = {}

with open('day3_input.txt', 'r') as f:
    lines = f.readlines()
    
    grouplist = []

    for i in range(0, len(lines), 3):
        grouplist.append(lines[i:i+3])
    
    for group in grouplist:
        gpt1 = re.sub('\n', '', group[0])
        gpt2 = re.sub('\n', '', group[1])
        gpt3 = re.sub('\n', '', group[2])



        dup = list(set(gpt1) & set(gpt2) & set(gpt3))
        groupDup[gpt1+gpt2+gpt3] = dup[0]

        

total = 0

for item in groupDup.values():
    total += allAlphaValues[item]

print(total)




#PART 1

#create dictionary for all rucksacks and all duplicates
# allRucksacks = {}
# allDup = {}

#     for line in lines:
#         line = re.sub('\n', '', line)
#         allRucksacks[line] = allRucksacks.get(line, 0)

#         mid = int(len(line)/2)
#         cpt1 = line[:mid]
#         cpt2 = line[mid:]

#         dup = list(set(cpt1).intersection(cpt2))
#         allDup[line] = dup[0]
    

# total = 0

# for item in allDup.values():
#     total += allAlphaValues[item]

# print(total)





