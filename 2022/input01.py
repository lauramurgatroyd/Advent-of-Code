print("PUZZLE 1 --------------------------------------------------------")
totals = []
with open("input01.txt") as input_file:
    current_total = 0
    for l in input_file:
        if l!= '\n':
            current_total += int(l)
        else:
            totals.append(current_total)
            current_total = 0
totals.append(current_total)
print(max(totals))

print("PUZZLE 2 --------------------------------------------------------")
sorted_totals = sorted(totals, reverse=True)
print(sum(sorted_totals[:3]))
