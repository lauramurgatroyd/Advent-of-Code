import numpy as np

print("PUZZLE 1 --------------------------------------------------------")

rules=[]
lines = 0
with open("Puzzle7_Input.txt") as input_file:
    for l in input_file:
        if l != '\n':
            l=l.strip('\n')
            l=l.split('bags contain')
            rules.append(l)
bag_colours = []
for rule in rules:
    if 'shiny gold' in rule[1]:
        bag_colours.append(rule[0])

bag_colours = list(dict.fromkeys(bag_colours))

old_len=len(bag_colours)
current_len=0
while current_len != old_len:
    old_len = current_len
    for rule in rules:
        for bag_colour in bag_colours:
            if bag_colour in rule[1]:
                bag_colours.append(rule[0])
    bag_colours = list(dict.fromkeys(bag_colours))
    current_len = len(bag_colours)
    #print(bag_colours)

print("number of colours: ", len(bag_colours))

print("PUZZLE 2 --------------------------------------------------------")

class Bag():
    def __init__(self,colour, num, prev, final = False):
        self.colour =colour
        if 'no' in str(num):
            self.num = 0
        else:
            self.num = int(num)
        if prev == []:
            self.prev = None
        else:
            self.prev = prev

        self.final = final




bags = [[Bag('shiny gold',1,None)]]
old_len=0
current_len=len(bags)

# try:
while current_len != old_len:
    current_bags=[]
    old_len = current_len
    for rule in rules:
        for i, bag in enumerate(bags[-1]):
                if bag.colour == rule[0].strip(' '):
                    contents = rule[1].split(',')
                    contents = [x[1:].strip('.') for x in contents]
                    contents = [x.strip('bags') for x in contents]
                    contents = [x.strip(' ') for x in contents]
                    if bag.num == None:
                        prev_num = 1
                    else:
                        prev_num = bag.num

                    
                    for x in contents:
                        if not 'no' in str(x[:2]):
                            # print([x[2:],int(x[:2])*prev_num, bag])
                            current_bags.append(Bag(x[2:],int(x[:2])*prev_num, bag))
                        else:
                            bag.final = True

    if len(current_bags) != 0:            
        bags.append(current_bags)
        current_bags = []
    current_len = len(bags)


bags_no=0
for i in range(len(bags)):
    for j in range(len(bags[i])):
        bags_no+= bags[i][j].num


print("Number of bags we need: ", bags_no-1)

#TODO: learn regex

