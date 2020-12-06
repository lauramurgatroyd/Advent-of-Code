import numpy as np

print("PUZZLE 1 --------------------------------------------------------")

groups=[]
lines = 0
current_group=""
with open("Puzzle6_Input.txt") as input_file:
    for l in input_file:
        if l != '\n':
            l=l.strip('\n')
            current_group+=l
            
        else:
            groups.append(current_group)
            current_group=""
    groups.append(current_group)



groups = ["".join(set(x)) for x in groups]

length_sum = 0

for i in groups:
    length_sum+=len(i)

print("The answer is: ", length_sum)

print("PUZZLE 2 --------------------------------------------------------")

groups=[]
lines = 0
current_group=[]
with open("Puzzle6_Input.txt") as input_file:
    for l in input_file:
        if l != '\n':
            l=l.strip('\n')
            current_group.append(l)
            
        else:
            groups.append(current_group)
            current_group=[]
    groups.append(current_group)

q_total=0
for group in groups:
    for i, person in enumerate(group):
        if i ==0:
            person_1=person
        else:
            for ans in person_1:
                if ans not in person:
                    person_1 =person_1.replace(ans, "")
    q_total+=len(person_1)


print("The answer is: ", q_total)

