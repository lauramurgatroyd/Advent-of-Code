from itertools import combinations 

print("PUZZLE 1 --------------------------------------------------------")
nums = []
with open("Puzzle1_Input.txt") as input_file:
    for l in input_file:
        nums.append(int(l))
combo_list = combinations(nums,2)
for pair in combo_list:
    pair_sum = sum(pair)
    if pair_sum == 2020:
        print("The pair is: ", pair)
        print("The 1st answer is: ", pair[0]*pair[1])

print("PUZZLE 2 --------------------------------------------------------")
combo_list = combinations(nums, 3)
for triple in combo_list:
    triple_sum = sum(triple)
    if triple_sum == 2020:
        print("The triple is: ", triple)
        print("The answer is: ", triple[0]*triple[1]*triple[2])

