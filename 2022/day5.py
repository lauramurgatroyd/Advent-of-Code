import numpy as np
sum=0
correct_rows = []
instructions = False
instruction_list = []
with open('input5.txt') as input:
    for l in input:
        if l != '\n' and instructions == False:
            correct_row = []
            #print("l: ", [l])
            l = l.strip('\n').split(' ')
            #print(l)
            index = 0
            while index < len(l):
                if l[index] == '':
                    correct_row.append('')
                    index+=4
                else:
                    correct_row.append(l[index])
                    index+=1
            correct_rows.append(correct_row)
        elif instructions:
            instruction_list.append(l.strip('\n').split(' '))
        else:
            #print("Instructions = True")
            instructions = True
number_of_stacks = len(correct_rows[0])
correct_rows.pop(-1)
#print(correct_rows)
#print(instruction_list)
#print(correct_rows[0][:])
stacks = []
# for i in range(number_of_stacks):
#     print(np.shape(correct_rows))
shape = np.shape(correct_rows)

for j in range(shape[1]):
    stack = []
    for k in range(shape[0]):
        if correct_rows[k][j] != '':
            stack.append(correct_rows[k][j].strip('[').strip(']'))
    stacks.append(stack)
#print(stacks)

#print(instruction_list)


for l in instruction_list:
    items_to_move = int(l[1])
    start_index = int(l[3])-1
    end_index = int(l[-1]) -1
    for i in range(items_to_move):
        item = stacks[start_index].pop(0)
        stacks[end_index].insert(0, item)

#print(stacks)

result = [i[0] for i in stacks]
#print(result)

string = ''
for i in result:
    string+=i
print(string)

print('----------------')

sum=0
correct_rows = []
instructions = False
instruction_list = []
with open('input5.txt') as input:
    for l in input:
        if l != '\n' and instructions == False:
            correct_row = []
            #print("l: ", [l])
            l = l.strip('\n').split(' ')
            #print(l)
            index = 0
            while index < len(l):
                if l[index] == '':
                    correct_row.append('')
                    index+=4
                else:
                    correct_row.append(l[index])
                    index+=1
            correct_rows.append(correct_row)
        elif instructions:
            instruction_list.append(l.strip('\n').split(' '))
        else:
            #print("Instructions = True")
            instructions = True
number_of_stacks = len(correct_rows[0])
correct_rows.pop(-1)
#print(correct_rows)
#print(instruction_list)
#print(correct_rows[0][:])
stacks = []
# for i in range(number_of_stacks):
#     print(np.shape(correct_rows))
shape = np.shape(correct_rows)

for j in range(shape[1]):
    stack = []
    for k in range(shape[0]):
        if correct_rows[k][j] != '':
            stack.append(correct_rows[k][j].strip('[').strip(']'))
    stacks.append(stack)
#print(stacks)

#print(instruction_list)


for l in instruction_list:
    items_to_move = int(l[1])
    start_index = int(l[3])-1
    end_index = int(l[-1]) -1
    for i in reversed(range(items_to_move)):
        item = stacks[start_index].pop(i)
        stacks[end_index].insert(0, item)

#print(stacks)

result = [i[0] for i in stacks]
#print(result)

string = ''
for i in result:
    string+=i
print(string)



 