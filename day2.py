import re

grand_total = 0
count = {}
value = {}

def score(play):
    abckey = None
    total = 0
    
    ascore = {'X': 'C', 'Y': 'A', 'Z': 'B'}
    bscore = {'X': 'A', 'Y': 'B', 'Z': 'C'}
    cscore = {'X': 'B', 'Y': 'C', 'Z': 'A'}

    abcscore = {'A': 1, 'B': 2, 'C': 3}
    xyzscore = {'X': 0, 'Y': 3, 'Z': 6}

    play = list(play)
    player1 = play[0]
    player2 = play[-1]

    

    if player1 == 'A':
        abckey = ascore[player2]
        
    
    elif player1 == 'B':
        abckey = bscore[player2]
    
    else:
        abckey = cscore[player2]
    
    total = abcscore[abckey] + xyzscore[player2]
    print(total)


    return total



with open('day2_input.txt', 'r') as f:
    lines = f.readlines()

    for line in lines:
        line = re.sub('\n', '', line)     
        count[line] = count.get(line, 0) + 1
    

plays = count.keys()

play_value = {}
for play in plays:
    play_value[play] = score(play)


for item in count:
    subtotal = count[item] 
    multiplier = play_value[item]
    
    ttotal = subtotal * multiplier
    grand_total += ttotal

print(grand_total)


#####PART 1


# def score(play):
#     total = 0
#     xyzscores = {'X': 1, 'Y': 2, 'Z': 3}
#     x_scores = {'A': 3, 'B': 0, 'C': 6}
#     y_scores = {'A': 6, 'B': 3, 'C': 0}
#     z_scores = {'A': 0, 'B': 6, 'C': 3}

#     play = list(play)
#     player1 = play[0]
#     player2 = play[-1]

#     total += xyzscores[player2]

#     if player2 == 'X':
#         total += x_scores[player1]
    
#     elif player2 == 'Y':
#         total += y_scores[player1]
    
#     else:
#         total += z_scores[player1]

#     return total


# with open('test.txt', 'r') as f:
#     lines = f.readlines()

#     for line in lines:
#         line = re.sub('\n', '', line)     
#         count[line] = count.get(line, 0) + 1
    

# plays = count.keys()

# play_value = {}
# for play in plays:
#     play_value[play] = score(play)
    

# for item in count:
#     subtotal = count[item] 
#     multiplier = play_value[item]
    
#     ttotal = subtotal * multiplier
#     grand_total += ttotal

# print(grand_total)



    
    













    

