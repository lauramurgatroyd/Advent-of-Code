import numpy as np
import random

print("PUZZLE 1 -----------------------------------------------------")
nums = []
with open("Puzzle10_Input.txt") as input_file:
    for l in input_file:
        nums.append(int(l))

nums = np.sort(nums)
# print(nums)

jolt_diffs = []
for i,n in enumerate(nums):
    if (i+1) < len(nums):
        jolt_diff = nums[i+1]-nums[i]
        jolt_diffs.append(jolt_diff)
# print(jolt_diffs)

print("The 3 jolt diffs times the 1 jolt diffs are: ", (jolt_diffs.count(3)+1)*(jolt_diffs.count(1)+1)) #1984 is too low

print("PUZZLE 2 -----------------------------------------------------")
def swapPositions(list, pos1, pos2): 
    list[pos1], list[pos2] = list[pos2], list[pos1] 
    return list

# start = 0
# end = nums[-1]+3
# orders = []
# order = []

# counter = 0
# while counter < 1e10:
#     counter+=1
#     random.shuffle(nums)
#     counter2 = 0
#     while len(order) < len(nums):
#         counter2+=1
#         for num in nums:
#             if num-start <=3:
#                 order.append(num)
#                 start = num
#         if counter2 > 1e10:
#             break
#     if len(order) == len(nums):
#         if order[-1] + 3 == end:
#             orders.append(order)

# print("Combos: ", len(orders))
orders=0
for i, jolt_diff in enumerate(jolt_diffs):
    if jolt_diff == 1:
        orders+=1
    # if jolt_diff ==1 and jolt_diffs[i] ==1:
    #     orders+=1

print(orders**2)
        
    




#Ans = 19026