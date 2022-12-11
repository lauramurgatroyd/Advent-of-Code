import numpy as np
sum=0
with open('input4.txt') as input:
    for l in input:
        l = l.split(',')
        #print(l)
        l = [m.split('-') for m in l]
        range1 = [int(m) for m in l[0]]
        range2 = [int(m) for m in l[1]]
        range1 = [j for j in range(range1[0], range1[1]+1)]
        range2 = [j for j in range(range2[0], range2[1]+1)]
        #print(range1, range2)
        #print(l)
        if len(range1) > len(range2):
            longest = range1
            shortest = range2
        else:
            shortest = range1
            longest = range2
        add_one=True
        for s in shortest:
            if s not in longest:
                add_one=False
                break
        if add_one:
            sum+=1
print(sum)

print('#----------------------------------------')

import numpy as np
sum=0
with open('input4.txt') as input:
    for l in input:
        l = l.split(',')
        #print(l)
        l = [m.split('-') for m in l]
        range1 = [int(m) for m in l[0]]
        range2 = [int(m) for m in l[1]]
        range1 = [j for j in range(range1[0], range1[1]+1)]
        range2 = [j for j in range(range2[0], range2[1]+1)]
        #print(range1, range2)
        #print(l)
        if len(range1) > len(range2):
            longest = range1
            shortest = range2
        else:
            shortest = range1
            longest = range2
        add_one=False
        for s in shortest:
            if s in longest:
                add_one=True
                break
        if add_one:
            sum+=1
print(sum)
        # get whichever is longer
        # for i in shortest, if all in longest add 1
#         print(l)

#         print(l)
#         first_letters=[]
#         num_items = len(l)
#         print("items: ", num_items)
#         for i, letter in enumerate(l):
#             if i < np.floor(num_items/2):
#                 first_letters.append(letter)
#             else:
#                 #print(first_letters)
#                 if letter in first_letters:
#                     #print(letter)
#                     print(first_letters)
#                     if letter.lower() == letter:
#                         sum+=ord(letter) - 96
#                         break
#                     else:
#                         sum+=ord(letter)-65+27
#                         break
#                     print(letter, sum)


# print(sum)

# #-------------------------------2

# print("puzzle 2")
# sum=0
# with open('input3.txt') as input:
#     i=0
#     current_bags = []
#     for l in input:
#         if i<2:
#             current_bags.append(l)
#             i+=1
#         elif i==2:
#             current_bags.append(l)
#             common_items = [j for j in current_bags[0] if j in current_bags[1] and j in current_bags[2]]
#             letter = common_items[0]
#             print(letter)
#             if letter.lower() == letter:
#                 sum+=ord(letter) - 96
#             else:
#                 sum+=ord(letter)-65+27
#             i=0
#             current_bags = []

# print(sum)
    