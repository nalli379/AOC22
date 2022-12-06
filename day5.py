import re
from collections import deque

arr = []
stacks={}

with open('day5_input.txt', 'r') as f:
    lines = f.readlines()
    char_map = {
        ord('\n'): '',
        ord('['): ' ',
        ord(']'): ' '
    }

    for line in lines:
        line = list(line.translate(char_map))
        arr.append(line)

arr.reverse()

stackLabel = arr[0]
labelIndex = {}

for i in range(len(stackLabel)):
    if stackLabel[i] != ' ':
        labelIndex[stackLabel[i]] = i
        stacks[stackLabel[i]] = []

arr = arr[1:]


stackNum = list(labelIndex.keys())
columns = list(labelIndex.values())

for row in arr:
    for i in range(len(columns)):
        if row[columns[i]] != ' ':
            box = row[columns[i]]
            stacks[stackNum[i]].append(box)

moves = []

with open('day5_input2.txt', 'r') as f:
    lines = f.readlines()

    for line in lines:
        line = line.replace('move ', '')
        line = line.replace('from ', '')
        line = line.replace('to ', '')
        line = line.replace('\n', '')
        line = line.split(' ')
        line = [int(line[0]), line[1], line[2]]
        moves.append(line)

for move in moves:
    
    if move[0] == 1:
        movebox = stacks[move[1]].pop()
        stacks[move[2]].append(movebox)
    
    elif move[0] > 1:
        smallStack = list(stacks[move[1]].pop() for _ in range(move[0]))
        stacks[move[2]].extend(reversed(smallStack))


toplist = []
fulllist = stacks.values()
for slist in fulllist:
    toplist.append(slist[-1])

print(''.join(toplist))


