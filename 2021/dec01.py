
nums = []
total=0
with open("dec01_input-1.txt") as input_file:
    for i, l in enumerate(input_file):
        nums.append(int(l))
        if i>0:
            if int(l)>nums[i-1]:
                total+=1

print(total)

# -----------------------------------------
nums = []
totals = []
with open("dec01_input-1.txt") as input_file:
    for i, l in enumerate(input_file):
        l=int(l)
        nums.append(l)
        if i>1:
            sum = nums[i-1]+l+nums[i-2]
            totals.append(sum)
total=0
for i, l in enumerate(totals):
    if l>totals[i-1]:
        total+=1
print(total)


