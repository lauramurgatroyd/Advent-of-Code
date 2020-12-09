
nums=[]

print("PUZZLE 1 --------------------------------------------------------")

with open("Puzzle9_Input.txt") as input_file:
    for l in input_file:
        if l != '\n':
            l=l.strip('\n')
            l=int(l)
            nums.append(l)

allowed=True
current_number = 0
preamble = 25
#preamble = 5

for i,num in enumerate(nums):
    allowed = False
    current_number = num
    #print(i)
    if i>(preamble-1):
        lower = i-preamble
        for j in range(lower,i):
            for k in range(lower,i):
                if k !=j:
                    #print(nums[j], nums[k], num)
                    if nums[j]+nums[k] == num:
                        allowed=True
                        #print(nums[j], nums[k], num)
    else:
        allowed = True
    if not allowed:
        break
        #print(allowed)
            
print("The first number that breaks the rule is: ", current_number)

print("PUZZLE 2 --------------------------------------------------------")

goal = current_number
sum_total = 0
nums_added= []
finished = False
for j in range(0,len(nums)):
    #print("new j ", j)
    for i in range(j, len(nums)):
        num = nums[i]
        if num+sum_total<=goal:
            if num<goal:
                sum_total+=num
                nums_added.append(num)
                #print(sum_total)
                if sum_total == goal:
                    print(nums_added)
                    finished = True
                    break
        else:
            sum_total = 0
            nums_added = []
            #print("loaser")
    if finished:
        break
    
    sum_total = 0
    nums_added = []
print(sum(nums_added))
print("Sum of smallest and biggest nums: ", min(nums_added)+ max(nums_added))




#must be lower than 116644310112772