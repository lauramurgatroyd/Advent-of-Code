import numpy as np
import copy

print("PUZZLE 1 -----------------------------------------------------")
seats = []
with open("Puzzle11_Input.txt") as input_file:
    for l in input_file:
        seats.append(l.strip('\n'))

#print(seats)

#print(len(seats[0]))


for i, seat_line in enumerate(seats):
    #print(seats[i])
    seats[i] = '.' + seats[i] + '.'
    seats[i] = list(seats[i])
seats.insert(0, ['.']*len(seats[0]))
seats.append(['.']*len(seats[0]))


old_seats = []
seating_unchanged = np.array_equal(old_seats, seats)
while not seating_unchanged:
    old_seats = copy.deepcopy(seats)
    for i, seat_line in enumerate(old_seats):
        if i >0 and i<(len(seats)-1):   
            for j, s in enumerate(seat_line):
                if j >0 and j<(len(seat_line)-1):
                    adjacent_occupied = 0
                    occupied = True
                    adjacent_seats = [old_seats[i][j-1], old_seats[i][j+1], old_seats[i-1][j], old_seats[i-1][j+1],old_seats[i-1][j-1], old_seats[i+1][j], old_seats[i+1][j-1], old_seats[i+1][j+1]]
                    if s == 'L':
                        for seat in adjacent_seats:
                            if seat == '#':
                                occupied = False
                    elif s == '#':
                        occupied = True
                        for seat in adjacent_seats:
                            if seat == '#':
                                adjacent_occupied +=1
                        if adjacent_occupied>3:
                            occupied = False
                    if s != '.':
                        if occupied:
                            seats[i][j] = '#'
                        else:
                            seats[i][j] = 'L'
    for seat_row in seats:
        string = ""
        for seat in seat_row:
            string = string + seat
        # print(string)
    #print("new round")

    seating_unchanged = np.array_equal(old_seats, seats)

occupied_seats = 0
for seat_row in seats:
    string = ""
    for seat in seat_row:
        string = string + seat
        if seat == '#':
            occupied_seats+=1
    # print(string)
print("The number of occupied seats: ", occupied_seats)

        
print("PUZZLE 2 -----------------------------------------------------")
seats = []
with open("Puzzle11_Input.txt") as input_file:
    for l in input_file:
        seats.append(l.strip('\n'))

#print(seats)

#print(len(seats[0]))


for i, seat_line in enumerate(seats):
    #print(seats[i])
    seats[i] = '.' + seats[i] + '.'
    seats[i] = list(seats[i])
seats.insert(0, ['.']*len(seats[0]))
seats.append(['.']*len(seats[0]))


old_seats = []
seating_unchanged = np.array_equal(old_seats, seats)
while not seating_unchanged:
    old_seats = copy.deepcopy(seats)
    for i, seat_line in enumerate(old_seats):
        if i >0 and i<(len(seats)-1):   
        # if i==1:
            for j, s in enumerate(seat_line):
                if j >0 and j<(len(seat_line)-1):
                #if j ==1:
                    adjacent_occupied = 0
                    occupied = True
                    adjacent_seats = [old_seats[i][j-1], old_seats[i-1][j-1], old_seats[i-1][j], old_seats[i][j+1], old_seats[i+1][j+1], old_seats[i+1][j], old_seats[i-1][j+1],old_seats[i+1][j-1]]
                    if i==1:
                        print(adjacent_seats)
                    seat_counters = [[i,j-1],[i-1, j-1], [i-1,j], [i,j+1], [i+1, j+1], [i+1,j], [i-1, j+1], [i+1, j-1]]
                    if old_seats[i][j] == '#' or old_seats[i][j] =='L':
                        for k in range (0, 8):
                            #print(k)
                            if k < 3:
                                add_on = -1
                            elif k <6:
                                add_on = 1
                            while adjacent_seats[k] == '.':
                                try:
                                    list_counters = seat_counters[k]
                                    for counter, c in enumerate(list_counters):
                                        #print("counter", counter, c)
                                        if (k == 7 and counter ==1) or (k==8 and counter ==0):
                                            list_counters[counter] = c+1
                                        elif (k==7 and counter ==0) or (k==8 and counter ==1):
                                            list_counters[counter] = c-1
                                            if c-1<0:
                                                break
                                        else:
                                            if (counter==0 and c !=i) or (counter==1 and c!=j):
                                                list_counters[counter] = c+add_on
                                                if c+add_on <0:
                                                    break
                                    #print("out")
                                    seat_counters[k] = list_counters
                                    #if old_seats[list_counters[0]][list_counters[1]]:
                                    adjacent_seats[k] = old_seats[list_counters[0]][list_counters[1]]
                                    #print(adjacent_seats[k])
                                except Exception:
                                    #print("exc", adjacent_seats[k])
                                    break

                    if i == 1:
                        print("ADJ SEATS:", adjacent_seats)
                        print(seat_counters)
                    
                    if s == 'L':
                        for seat in adjacent_seats:
                            if seat == '#':
                                occupied = False
                    elif s == '#':
                        occupied = True
                        for seat in adjacent_seats:
                            if seat == '#':
                                adjacent_occupied +=1
                        if adjacent_occupied>4:
                            occupied = False
                    if s != '.':
                        if occupied:
                            seats[i][j] = '#'
                        else:
                            seats[i][j] = 'L'
    for seat_row in seats:
        string = ""
        for seat in seat_row:
            string = string + seat
        print(string)
    print("new round")

    seating_unchanged = np.array_equal(old_seats, seats)
occupied_seats = 0
for seat_row in seats:
    string = ""
    for seat in seat_row:
        string = string + seat
        if seat == '#':
            occupied_seats+=1
    print(string)
print("The number of occupied seats: ", occupied_seats)