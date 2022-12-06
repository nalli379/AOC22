
#read a text file 
#iterate over each group of values
#use the space to separate values
#to create a sum value, add sum to list
#compare that value to a max value, if it is higher than max, switch to new max
#return the max value


all_calories = {}
index = 0


with open('day1_input.txt', 'r') as f:
    lines = f.readlines()

    for line in lines:
        if line != '\n':
            all_calories[index] = all_calories.get(index, 0) + int(line)
        else:
            index += 1

list_calories = sorted(list(all_calories.values()), reverse=True)

top_3 = 0
for i in range(3):
    top_3 += list_calories[i]



