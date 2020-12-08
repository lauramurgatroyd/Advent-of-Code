rules = []

print("PUZZLE 1 --------------------------------------------------------")

with open("Puzzle8_Input.txt") as input_file:
    for l in input_file:
        if l != '\n':
            l=l.strip('\n')
            l=l.split(' ')
            l.append(False)
            l.append('')
            rules.append(l)


current_rule = 0
acc=0

order_visited = []

try:
    while not rules[current_rule][2]:
        order_visited.append(rules[current_rule])
        rules[current_rule][2]= True
        if rules[current_rule][0] == 'nop':
            current_rule+=1
            rules[current_rule][3]=current_rule
        elif rules[current_rule][0] == 'acc':
            acc+=int(rules[current_rule][1])
            current_rule+=1
            rules[current_rule][3] = current_rule
        elif rules[current_rule][0] == 'jmp':
            current_rule+=int(rules[current_rule][1])
            rules[current_rule][3] = current_rule
except Exception as e:
    pass

print("The acc when the loop starts is: ", acc)

print("PUZZLE 2 --------------------------------------------------------")
# ---------------------------------------------------------------------------------
rules=[]
with open("Puzzle8_Input.txt") as input_file:
    for l in input_file:
        if l != '\n':
            l=l.strip('\n')
            l=l.split(' ')
            l.append(False)
            l.append(False)
            l.append('')
            rules.append(l)


exc = False
acc=0
rule_no = 0

while not exc:
    for i, rule in enumerate(rules):
        if not rule[4]:
            if rule[0] == 'jmp':
                rules[i][0] = 'nop'
                rules[i][4] = True
                rule_no = i
                break
            elif rule[0] == 'nop':
                rules[i][0] = 'jmp'
                rules[i][4] =  True
                rule_no = i
                break
    acc = 0
    current_rule = 0

    try:
        # print("FIRST",rules[current_rule][2] )
        while not rules[current_rule][2]:
            order_visited.append(rules[current_rule])
            #print(rules[current_rule])
            rules[current_rule][2]= True
            if rules[current_rule][0] == 'nop':
                current_rule+=1
                rules[current_rule][3]=current_rule
            elif rules[current_rule][0] == 'acc':
                acc+=int(rules[current_rule][1])
                #print(acc)
                current_rule+=1
                rules[current_rule][3] = current_rule
                
            elif rules[current_rule][0] == 'jmp':
                current_rule+=int(rules[current_rule][1])
                rules[current_rule][3] = current_rule
    except Exception as e:
        #print(e)
        exc = True
    if rules[i][0] == 'jmp':
        rules[i][0] = 'nop'

    elif rule[0] == 'nop':
        rules[i][0] = 'jmp'
    # if acc>0:
    #     print("try again", acc)
    # print(order_visited)
    for i, rule in enumerate(rules):
        rules[i][2]=False


print("The final acc is: ", acc)


#TODO: tidy the below and check why it failed
# # print("The acc when the loop starts is: ", acc) #but we need to make it so there is no loop
# rule_no = 655
# file_end = 655
# # rule_no = 10
# #file_end=10
# done = False
# # while not done:
# possible_rule_ends = []
# for i,rule in enumerate(rules):
#     rule_no = i+1
#     rule[3]=rule_no
#     if int(rule[1])+i+1 >= file_end:
#         #print(rule)
#         if rule[0] != 'acc':
#             possible_rule_ends.append(rule)
#         # if rule[0] == 'nop':
#         #     done=True
#         #print(rule_no)

# print(possible_rule_ends)
# #print(rules)

# # for rule_end in possible_rule_ends:
# rule_no = possible_rule_ends[0][3]
# print(rule_no)
# visited=[rule_no]

# print("Starting the loop")
# while not done:
#     #print("REP AGAIN", rule_no)
#     for i,rule in enumerate(rules):
#         if rule[0] == 'acc':
#             if int(rule[3])+1 == rule_no:
#                 rule_no = int(rule[3])
#                 print(rule)
#         elif rule[0] == 'nop':
#             if int(rule[3])+1 == rule_no:
#                 rule_no = int(rule[3])
#                 print(rule)
#             elif int(rule[1])+int(rule[3]) == rule_no:
#                 print(rule)
#                 rule_no = i+1
#                 # if rule[0] == 'nop':
#                 done=True
#                 print(rules[rule_no-1][0])
#                 rules[rule_no-1][0]='jmp'
#                 print(rules[rule_no-1][0])
#                 #     print(rule)
#         else:
#             #print(int(rule[1])+int(rule[3]))
#             if int(rule[1])+int(rule[3]) == rule_no:
#                 print(rule)
#                 rule_no = i+1
#                 # if rule[0] == 'nop':
#                 #     done=True
#                 #     print(rule)
#             elif int(rule[3])+1 == rule_no:
#                 print(rule)
#                 rule_no = i+1
#                 # if rule[0] == 'nop':
#                 done=True
#                 print(rules[rule_no-1][0])
#                 rules[rule_no-1][0]='nop'
#                 print(rules[rule_no-1][0])
#         #visited.append(rule_no)
# # ---------------------------------------



# # remember that we have to check if the line before is acc or nop because then they will go to that line
# current_rule = 0
# while current_rule< len(rules):
#     #print(current_rule)
#     if rules[current_rule][0] == 'nop':
#         current_rule+=1
#         rules[current_rule][3]=current_rule
#     elif rules[current_rule][0] == 'acc':
        
#         acc+=int(rules[current_rule][1])
#         current_rule+=1
#         rules[current_rule][3] = current_rule
#     elif rules[current_rule][0] == 'jmp':
#         current_rule+=int(rules[current_rule][1])
#         rules[current_rule][3] = current_rule
#     #print(acc)

#print("The acc when the loop starts is: ", acc)


    