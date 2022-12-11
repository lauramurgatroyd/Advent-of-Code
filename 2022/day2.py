print("PUZZLE 1 --------------------------------------------------------")
points_per_letter = {'X': 1, 'Y': 2, 'Z': 3} # rock, paper, scissors
points_per_win = 6
points_per_draw = 3
points_per_loss = 0
points = {('A', 'X'): points_per_draw, ('A', 'Y'): points_per_win, ('A', 'Z'): points_per_loss, ('B', 'X'): points_per_loss, ('B', 'Y'): points_per_draw, ('B', 'Z'): points_per_win, ('C', 'X'): points_per_win, ('C', 'Y'): points_per_loss, ('C', 'Z'): points_per_draw}
total_points = 0
with open("input02.txt") as input_file:
    print(input_file)
    for l in input_file:
        if l != '\n':
            l=l.strip('\n')
            l=l.split(" ")
            l = tuple(l)
            points_this_round = points[l]
            points_this_round+= points_per_letter[l[1]]
            total_points += points_this_round
print(total_points)

print("PUZZLE 2 --------------------------------------------------------")
points_per_letter = {'X': 1, 'Y': 2, 'Z': 3} # rock, paper, scissors
win_loss_translation = {'X': points_per_loss, 'Y': points_per_draw, 'Z': points_per_win}
outcomes_per_letter = { \
    'A':{points_per_win: 'Y', points_per_draw: 'X', points_per_loss: 'Z'}, \
    'B':{points_per_win: 'Z', points_per_draw: 'Y', points_per_loss: 'X'}, \
    'C':{points_per_win: 'X', points_per_draw: 'Z', points_per_loss: 'Y'}}
total_points = 0
with open("input02.txt") as input_file:
    print(input_file)
    for l in input_file:
        if l != '\n':
            l=l.strip('\n')
            l=l.split(" ")
            l = tuple(l)
            points_this_round = win_loss_translation[l[1]] + points_per_letter[outcomes_per_letter[l[0]][win_loss_translation[l[1]]]]
            # points_this_round = points[l]
            # points_this_round+= points_per_letter[l[1]]
            total_points += points_this_round
print(total_points)

#------------------------------------------------------------
# f = lambda x: ('  BXCYAZAXBYCZCXAYBZ'.index(x[0]+x[2]),
#                '  BXCXAXAYBYCYCZAZBZ'.index(x[0]+x[2]))

# print(*[sum(x)//2 for x in zip(*map(f, open('in.txt')))])