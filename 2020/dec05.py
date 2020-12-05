from itertools import combinations 
import numpy as np

print("PUZZLE 1 --------------------------------------------------------")

id_list=[]
lines = 0
with open("Puzzle5_Input.txt") as input_file:
    for l in input_file:
        board_no = [l[:7], l[7:].strip('\n')]
        # print(pass_list)
        y_range = [0, 127] # 0 to 127
        for y in board_no[0]:
            half_range = (y_range[1] - y_range[0]+1)/2
            if y == 'F':
                y_range[1]=half_range-1+y_range[0]
            if y=='B':
                y_range[0] += half_range
        y_no = y_range[0]
        x_range = [0,7]
        for x in board_no[1]:
            half_range = (x_range[1] - x_range[0]+1)/2
            if x == 'L':
                x_range[1]=half_range-1+x_range[0]
            if x=='R':
                x_range[0] += half_range
        
        x_no = x_range[0]
        #print(x_no, y_no)
        id_no = y_no*8+x_no
        id_list.append(id_no)
#print(id_list)
print("The ax ID number is: ", int(max(id_list)))

print("PUZZLE 2 --------------------------------------------------------")
seat = 0
id_list.sort()
for i, val in enumerate(id_list):
    current_id = val
    if i>0:
        if current_id - last_id ==2:
            seat = (current_id-1)
    last_id = current_id

print("The seat number is: ", int(seat))

