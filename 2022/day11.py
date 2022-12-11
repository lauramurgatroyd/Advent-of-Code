import numpy as np
print("PUZZLE 1 --------------------------------------------------------")
holding = {}
operation = {}
test = {}
true_result = {}
false_result = {}
monkey_num = 0
with open("day11.txt") as input_file:
    for l in input_file:
        if l == '\n':
            monkey_num += 1
        else:
            l = l.strip('\n')
            if "Starting items" in l:
                l = l.replace("Starting items: ", "")
                holding[monkey_num] = l.split(", ")
            elif "Operation: " in l:
                l = l.replace("Operation: new = old ", "")
                operation[monkey_num] = l
            elif "Test" in l:
                l = l.replace("Test: divisible by ", "")
                test[monkey_num] = l
            elif "true" in l:
                l = l.replace("If true: throw to monkey ", "")
                true_result[monkey_num] = l
            elif "false" in l:
                l = l.replace("If false: throw to monkey ", "")
                false_result[monkey_num] = l
monkey_num+=1
rounds = 20
inspections = {x: 0 for x in range(0, monkey_num)}
for round in range(0, rounds):
    print("round ", round)
    for monkey in range(0, monkey_num):
        items = holding[monkey]
        inspections[monkey] += len(items)
        for item in items:
            print(item, operation[monkey])
            old = int(item)
            print(eval(item +  operation[monkey]))
            worry = int(np.floor(eval(item +  operation[monkey])/3))
            if worry % int(test[monkey]) == 0:
                holding[int(true_result[monkey])].append(str(int(worry)))
                print("Item with worry level {} is thrown to {}.".format(worry, monkey))
            else:
                holding[int(false_result[monkey])].append(str(int(worry)))
                print("Item with worry level {} is thrown to {}.".format(worry, monkey))
        holding[monkey] = []

print("inspecs ", inspections)
print(holding)

highest_value = 0
highest_value_key = ""
for key, value in inspections.items():
    if value > highest_value:
        highest_value = value
        highest_value_key = key
inspections.pop(highest_value_key)
second_highest_value = 0
second_highest_value_key = ""
for key, value in inspections.items():
    if value > second_highest_value:
        second_highest_value = value
        second_highest_value_key = key
print("part 1 ", highest_value*second_highest_value)

print("PUZZLE 2 --------------------------------------------------------")

rounds = 10000
inspections = {x: 0 for x in range(0, monkey_num)}
for round in range(0, rounds):
    print("round ", round)
    for monkey in range(0, monkey_num):
        items = holding[monkey]
        inspections[monkey] += len(items)
        for item in items:
            #print(item, operation[monkey])
            old = int(item)
            #print(eval(item +  operation[monkey]))
            worry = int(np.floor(eval(item +  operation[monkey])))
            if worry % int(test[monkey]) == 0:
                holding[int(true_result[monkey])].append(str(int(worry)))
                #print("Item with worry level {} is thrown to {}.".format(worry, monkey))
            else:
                holding[int(false_result[monkey])].append(str(int(worry)))
                #print("Item with worry level {} is thrown to {}.".format(worry, monkey))
        holding[monkey] = []

print("inspecs ", inspections)
print(holding)

highest_value = 0
highest_value_key = ""
for key, value in inspections.items():
    if value > highest_value:
        highest_value = value
        highest_value_key = key
inspections.pop(highest_value_key)
second_highest_value = 0
second_highest_value_key = ""
for key, value in inspections.items():
    if value > second_highest_value:
        second_highest_value = value
        second_highest_value_key = key
print("part 1 ", highest_value*second_highest_value)

