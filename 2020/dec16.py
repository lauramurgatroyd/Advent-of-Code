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

print(ranges)
print(nearby_tickets)

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
