from itertools import combinations 

print("PUZZLE 1 --------------------------------------------------------")
successes = 0
with open("Puzzle2_Input.txt") as input_file:
    for l in input_file:

        password_array = l.strip("\n").split(" ")
        char_num_range = password_array[0].split('-')
        char_num_range = [int(x) for x in char_num_range]
        char = password_array[1].strip(':')
        password = password_array[2]
        
        instances = password.count(char)
        if instances in range(char_num_range[0], char_num_range[1]+1):
            # print(char_num_range)
            # print(char)
            # print(password)
            successes+=1

print("The number of successful passwords is: ", successes)

print("PUZZLE 2 --------------------------------------------------------")
successes = 0
with open("Puzzle2_Input.txt") as input_file:
    for l in input_file:

        password_array = l.strip("\n").split(" ")
        char_num_range = password_array[0].split('-')
        char_num_range = [int(x) for x in char_num_range]
        char = password_array[1].strip(':')
        password = password_array[2]

        count = 1 
        locations = []
        for l in password:
            if l == char:
                locations.append(count)
            count+=1
            
        if (char_num_range[0] in locations and not char_num_range[1] 
                in locations) or (char_num_range[1] in locations and 
                not char_num_range[0] in locations):
            # print(char_num_range)
            # print(locations)
            successes+=1

print("The number of successful passwords is: ", successes)



