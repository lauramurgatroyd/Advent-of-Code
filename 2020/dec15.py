print("PUZZLE 1 --------------------------------------------------------")
start = [0, 3, 6]
read_numbers = [0, 3, 6]
count = 0
target_element = 2020
while len(read_numbers) < target_element:
    current_num = read_numbers[-1]
    location = len(read_numbers)-1
    read_numbers.reverse()
    # print(read_numbers)
    for i, val in enumerate(read_numbers):
        if i > 0:
            if val == current_num:
                location = len(read_numbers)-1-i
                break
    read_numbers.reverse()
    diff = len(read_numbers)-location-1
    read_numbers.append(diff)
    # print(read_numbers)

#print(read_numbers)
print(read_numbers[-1])

print("PUZZLE 2 --------------------------------------------------------")
start = [0, 3, 6]

read_numbers=[13,0,10,12,1,5,8]
#read_numbers = [0, 3, 6]
count = 0
target_element = 30000000
#target_element = 2020
nums_dict = {}
for i, num in enumerate(read_numbers):
    nums_dict.update({num: i})
#print(nums_dict)
while len(read_numbers) < target_element:
    count+=1
    if count%1000000 ==0:
        print(count/30000000 *100, "%")
    current_num = read_numbers[-1]
    current_location = len(read_numbers)-1
    if current_num in nums_dict.keys():
        new_value= len(read_numbers)-1 -nums_dict[current_num]
    else:
        new_value = 0
    read_numbers.append(new_value)
    nums_dict.update({current_num: current_location})
    # print(nums_dict)
    # print(read_numbers)

# print(nums_dict)
# print(read_numbers)
print(read_numbers[-1])
