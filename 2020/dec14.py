import re
import copy
from itertools import combinations_with_replacement, permutations, product

print("PUZZLE 1 -----------------------------------------------------")
first_mask = True
current_rules = {}
mem_regex = re.compile(r"[\w]+\[([\w]+)\][\s]=[\s]([\w]+)")
with open("Puzzle14_Input.txt") as input_file:
    for line in input_file:
        if line.startswith("mask"):
            mask = list(line.split('=')[-1].strip())
        else:
            match = mem_regex.match(line)
            #print({match.group(1): match.group(2)})
            binary = bin(int(match.group(2)))[2:]
            # print(binary)
            if len(binary) < len(mask):
                diff = len(mask)-len(binary)
                binary = list('0'*diff + str(binary))

            for i, value in enumerate(mask):
                if value != 'X':
                    binary[i] = value
            binary_num = '0b'

            for i in binary:
                binary_num += i

            #print("bin", binary_num)
            dec = int(binary_num, 2)

            current_rules.update({match.group(1): str(dec)})

# print(current_rules)
sum_vals = 0
for s in current_rules.values():
    sum_vals += int(s)


print("The answer is: ", sum_vals)

print("PUZZLE 2 -----------------------------------------------------")
first_mask = True
current_rules = {}
mem_regex = re.compile(r"[\w]+\[([\w]+)\][\s]=[\s]([\w]+)")
count = 0
with open("Puzzle14_Input.txt") as input_file:
    for line in input_file:
        if line.startswith("mask"):
            mask = list(line.split('=')[-1].strip())
            count+=1
            #print(count)
        else:
            match = mem_regex.match(line)
            #print({match.group(1): match.group(2)})
            binary = bin(int(match.group(1)))[2:]
            # print(binary)
            if len(binary) < len(mask):
                diff = len(mask)-len(binary)
                binary = list('0'*diff + str(binary))

            for i, value in enumerate(mask):
                if value != '0':
                    binary[i] = value
      
            no_Xs=0
            for i in range(0, len(binary)):
                if binary[i] =='X':
                    no_Xs+=1
            #print("OG binary: ",  binary)
            x=[0,1]
            # options=[]
            # for c in combinations_with_replacement(x, no_Xs):
            #     for p in permutations(c,no_Xs):
            #         #print(p)
            #         if p not in options:
            #             options.append(list(p))
            # #print("Options", options)
            options = [list(p) for p in product(x, repeat=no_Xs)] 
            binaries=[]
            for option in options:
                current_binary= copy.deepcopy(binary)
                for i, c in enumerate(current_binary):
                    if c == 'X':
                        current_binary[i] = option.pop(0)
                binaries.append(current_binary)
                               
            binary_nums = []
            for binary in binaries:
                binary_num = '0b'
                for i in binary:
                    binary_num += str(i)
                binary_nums.append(binary_num)

            #print("bin", binary_num)
            decs = [int(binary_num, 2) for binary_num in binary_nums]

            for dec in decs:
                current_rules.update({str(dec): str(match.group(2))})
#print(current_rules)

sum_vals = 0
for s in current_rules.values():
    sum_vals += int(s)

print("The answer is: ", sum_vals)