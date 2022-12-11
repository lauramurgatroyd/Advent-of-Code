print("PUZZLE 1 --------------------------------------------------------")
with open("input06.txt") as input_file:
    print(input_file)
    for l in input_file:
        if l != '\n':
            l=l.strip('\n')
            print(l)
            for max in range(4, len(l)):
                min = max-4
                subset = l[min:max]
                print(subset)
                subset_list = []
                unique = True
                for i, c in enumerate(subset):
                    if c in subset_list:
                        unique = False
                        break
                    else:
                        subset_list.append(c)
                        
                if unique:
                    print("Result: ", max)
                    break

print("PUZZLE 2 --------------------------------------------------------")
length = 14
with open("input06.txt") as input_file:
    print(input_file)
    for l in input_file:
        if l != '\n':
            l=l.strip('\n')
            print(l)
            for max in range(length, len(l)):
                min = max-length
                subset = l[min:max]
                print(subset)
                subset_list = []
                unique = True
                for i, c in enumerate(subset):
                    if c in subset_list:
                        unique = False
                        break
                    else:
                        subset_list.append(c)
                        
                if unique:
                    print("Result: ", max)
                    break


