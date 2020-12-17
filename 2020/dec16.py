print("PUZZLE 1 -----------------------------------------------------")

ranges = {}

nearby_tickets = []

with open("Puzzle16_Input.txt") as input_file:
    ranges_section = True
    your_ticket_section = True
    other_ticket_section = False
    for line in input_file:
        if ranges_section:
            if line == '\n':
                ranges_section = False
                your_ticket_section = True
            else:
                line = line.strip().split(':')
                line[1] = line[1].split('or')
                for i, r in enumerate(line[1]):
                    line[1][i] = r.split('-')
                    line[1][i] = [int(x) for x in line[1][i]]
                ranges.update({line[0]: line[1]})
        elif your_ticket_section:
            if line == '\n':
                your_ticket_section = False
                other_ticket_section = True
        elif other_ticket_section:
            if 'nearby tickets:' not in line:
                line = line.strip().split(',')
                line = [int(x) for x in line]
                nearby_tickets.append(line)

for rule, range_lists in ranges.items():
    valid_numbers = []
    for r in range_lists:
        valid_array = [x for x in range(r[0], r[1]+1)]
        for x in valid_array:
            valid_numbers.append(x)
    ranges[rule] = valid_numbers

# print(ranges)
# print(nearby_tickets)

error_rate = 0
for ticket in nearby_tickets:
    for value in ticket:
        valid = False
        for rule, range_lists in ranges.items():
            if value in range_lists:
                valid = True
                break
        if not valid:
            error_rate += value

print("Error rate: ", error_rate)

print("PUZZLE 2 -----------------------------------------------------")

ranges = {}

nearby_tickets = []

departure_indices = []

my_ticket = []

with open("Puzzle16_Input.txt") as input_file:
    ranges_section = True
    your_ticket_section = True
    other_ticket_section = False
    count=0
    for line in input_file:
        if ranges_section:
            if line == '\n':
                ranges_section = False
                your_ticket_section = True
            else:
                line = line.strip().split(':')
                line[1] = line[1].split('or')
                for i, r in enumerate(line[1]):
                    line[1][i] = r.split('-')
                    line[1][i] = [int(x) for x in line[1][i]]
                ranges.update({count: line[1]})
                if 'departure' in line[0]:
                    departure_indices.append(count)
                count+=1
        elif your_ticket_section:
            if line == '\n':
                your_ticket_section = False
                other_ticket_section = True
            elif 'ticket' not in line:
                line = line.strip().split(',')
                line = [int(x) for x in line]
                my_ticket = line
        elif other_ticket_section:
            if 'nearby tickets:' not in line:
                line = line.strip().split(',')
                line = [int(x) for x in line]
                nearby_tickets.append(line)

for rule, range_lists in ranges.items():
    valid_numbers = []
    for r in range_lists:
        valid_array = [x for x in range(r[0], r[1]+1)]
        for x in valid_array:
            valid_numbers.append(x)
    ranges[rule] = valid_numbers

# print(ranges)
# print(nearby_tickets)

error_rate = 0
tickets_to_pop = []
for i, ticket in enumerate(nearby_tickets):
    for value in ticket:
        valid = False
        for rule, range_lists in ranges.items():
            if value in range_lists:
                valid = True
                break
        if not valid:
            error_rate += value
            tickets_to_pop.append(i)
tickets_to_pop.reverse()

# only want valid tickets:
for t in tickets_to_pop:
    nearby_tickets.pop(t)

ticket_dicts = [[] for x in nearby_tickets[0]]
for i, ticket in enumerate(nearby_tickets):
    if i == 0:
        for j, value in enumerate(ticket):
            count = 0
            for rule, range_lists in ranges.items():
                if value in range_lists:
                    ticket_dicts[j].append(count)
                    #print(j, count)
                    
                count+=1
    elif i>0:
        for j, value in enumerate(ticket):
            items_to_pop = []
            for rule_no in ticket_dicts[j]:
                if value not in ranges[rule_no]:
                    items_to_pop.append(rule_no)
            for item in items_to_pop:
                ticket_dicts[j].remove(item)
#print(ticket_dicts)
for i, possibles in enumerate(ticket_dicts):
    if len(possibles) == 1:
        for j, poss in enumerate(ticket_dicts):
            if j!=i:
                if possibles[0] in poss:
                    ticket_dicts[j].remove(possibles[0])


#print(ticket_dicts)

values = [x for x in range(0,len(my_ticket))]
sort_dict = {}
for x in values:
    sort_dict.update({x:[]})

finished = False
while not finished:
    #print(ticket_dicts)
    for i, thing in enumerate(ticket_dicts):
        for t in thing:
            sort_dict[t].append(i)
    for i, v in sort_dict.items():
        if len(v) == 1:
            ticket_dicts[v[0]] = [i]
            for j, poss in enumerate(ticket_dicts):
                if j!=v[0]:
                    if i in poss:
                        ticket_dicts[j].remove(i)
    for i, possibles in enumerate(ticket_dicts):
        if len(possibles) == 1:
            for j, poss in enumerate(ticket_dicts):
                if j!=i:
                    if possibles[0] in poss:
                        ticket_dicts[j].remove(possibles[0])
    finished = True
    for j in ticket_dicts:
        if len(j) != 1:
            finished = False
            break

# print(ticket_dicts)

ans = 1
# print(departure_indices)
ticket_dicts = [x[0] for x in ticket_dicts]
for d in departure_indices:
    ans*=my_ticket[ticket_dicts.index(d)]

print("The answer is: ", ans)

# if ans> 204376594109:
#     print("yay")

# 204376594109 is too low


