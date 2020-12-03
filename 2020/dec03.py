from itertools import combinations 
import numpy as np

print("PUZZLE 1 --------------------------------------------------------")

map_list=[]
lines = 0
with open("Puzzle3_Input.txt") as input_file:
    for l in input_file:
        map_list.append(list(l.strip('\n')))
        lines=lines+1
line_length = len(map_list[0])
map_list_length = len(map_list)

# Going 1 down, 3 right so...
# On each line we visit square 3n-2 where n is the line number
# So on the final line we need 3*map_list_length-2 squares

mult = int(np.ceil((3*map_list_length-2)/line_length))
map_list = [l*mult for l in map_list ]
trees = 0
for count, l in enumerate(map_list):
    if l[3*(count)] == '#':
        trees+=1

print("The number of trees is: ", trees)


print("PUZZLE 2 --------------------------------------------------------")

map_list=[]
lines = 0
with open("Puzzle3_Input.txt") as input_file:
    for l in input_file:
        map_list.append(list(l.strip('\n')))
        lines=lines+1
line_length = len(map_list[0])
map_list_length = len(map_list)

# Furtherst right we go is: Going 1 down, 7 right so...
# On each line we visit square 7n-6 where n is the line number
# So on the final line we need 7*map_list_length-6 squares

mult = int(np.ceil((7*map_list_length-6)/line_length))
map_list = [l*mult for l in map_list ]
trees = [0]*5
for count, l in enumerate(map_list):
    if l[count] == '#':
        trees[0]+=1
    if l[3*(count)] == '#':
        trees[1]+=1
    if l[5*(count)] == '#':
        trees[2]+=1
    if l[7*(count)] == '#':
        trees[3]+=1
    if count !=0 and count%2 ==0:
        if l[int(count/2)] == '#':
            trees[4]+=1

ans = 1
for i in trees:
    ans *= i

print("The answer is: ", ans)