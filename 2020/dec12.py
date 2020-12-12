
print("PUZZLE 1 -----------------------------------------------------")

directions = []
with open("Puzzle12_Input.txt") as input_file:
    for l in input_file:
        l= l.strip('\n')
        #print(l[0])
        if l[0] == 'N':
            l=l.replace("N", '0')
            #print(l, "replaced")
        if l[0] == 'E':
            l=l.replace("E", '1')
        if l[0] == 'S':
            l=l.replace("S", '2')
        if l[0]=='W':
            l=l.replace("W", '3')
        directions.append([l[0], int(l[1:])])
#print(directions)
distances = [0]*4
direction = 1
for l in directions: 
    try:
        l[0] = int(l[0])
        distances[l[0]]+=l[1]

    except Exception:
        if l[0] == 'F':
            # print(l[1])
            # print(direction)
            distances[direction]+=l[1]
        if l[0] == 'R':
            direction+=int(l[1]/90)
            while direction >3:
                direction-=4
        if l[0] =='L':
            direction-=int(l[1]/90)
            while direction<0:
                direction+=4
    #print(distances)
manhattan = abs(distances[1]-distances[3]) + abs(distances[2]-distances[0])
print("The manhattan distance is:", manhattan)


print("PUZZLE 2 -----------------------------------------------------")

directions = []
with open("Puzzle12_Input.txt") as input_file:
    for l in input_file:
        l= l.strip('\n')
        #print(l[0])
        if l[0] == 'N':
            l=l.replace("N", '0')
            #print(l, "replaced")
        if l[0] == 'E':
            l=l.replace("E", '1')
        if l[0] == 'S':
            l=l.replace("S", '2')
        if l[0]=='W':
            l=l.replace("W", '3')
        directions.append([l[0], int(l[1:])])
#print(directions)
og_distance = [1,10,0,0]
waypoint_location = [1,10,0,0]
ship_location = [0,0,0,0]
direction = 1
for l in directions: 
    try:
        l[0] = int(l[0])
        waypoint_location[l[0]] +=l [1]
    except Exception:
        if l[0] == 'F':
            # print(l[1])
            # print(direction)
            for direction in [0, 1, 2, 3]:
                current_ship_location = ship_location[direction]
                ship_location[direction] +=l[1]*(waypoint_location[direction]-ship_location[direction])
                waypoint_location[direction] +=l [1]*(waypoint_location[direction]-current_ship_location)
        if l[0] == 'R':
            turns = 0
            turns+=int(l[1]/90)
            waypoint_location=[waypoint_location[s] - ship_location[s] for s in range(0,4)]
            while turns>0:
                turns-=1
                waypoint_location = [waypoint_location[3], waypoint_location[0], waypoint_location[1], waypoint_location[2]]
            for m, loc in enumerate(ship_location):
                if loc !=0:
                    waypoint_location[m] = waypoint_location[m]+ loc
        if l[0] =='L':
            turns = 0
            turns+=int(l[1]/90)
            waypoint_location=[waypoint_location[s] - ship_location[s] for s in range(0,4)]
            while turns>0:
                turns-=1
                waypoint_location = [waypoint_location[1], waypoint_location[2], waypoint_location[3], waypoint_location[0]]
            for m, loc in enumerate(ship_location):
                if loc !=0:
                    waypoint_location[m] = waypoint_location[m]+ loc
    #print("ship: ", ship_location)
    #print("waypoint: ", waypoint_location)
relative_distances=[]
for x in og_distance:
    for y in distances:
        relative_distances.append(y-x)
manhattan = abs(ship_location[1]-ship_location[3]) + abs(ship_location[2]-ship_location[0])
print("The manhattan distance is:", manhattan)

