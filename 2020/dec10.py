import numpy as np

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

