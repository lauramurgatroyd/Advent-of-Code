print("PUZZLE 1 -----------------------------------------------------")
start_time = 0
buses = []
bus_arrived = False
import math

with open("Puzzle13_Input.txt") as input_file:
    start_time = int(input_file.readline())
    buses = input_file.readline().split(',')
current_time = start_time

buses = [int(b) for b in buses if b != 'x']

# for i, bus in enumerate(buses):
#         buses[i]=int(bus)
bus_number = 0
while not bus_arrived:
    for bus in buses:
        if current_time % bus == 0:
            bus_arrived = True
            bus_number = bus
            break
    current_time += 1

print("Bus number: ", bus_number)
print("Time: ", current_time-1)

print("The answer is: ", bus_number*(current_time-start_time-1))

print("PUZZLE 2 -----------------------------------------------------")
import time

real_start_time = time.time()
# print("Time: ", time)
#start_time = 100000000000000
start_time = 0
buses = []
bus_arrived = False


with open("Puzzle13_Input.txt") as input_file:
    start_time = int(input_file.readline())
    buses = input_file.readline().split(',')
start_time = 0
# current_time = 41*431

sequence = [False]*len(buses)
buses_dict = {} # index: bus no
for i, bus in enumerate(buses):
    if bus != 'x':
        buses[i] = int(bus)
        buses_dict.update({i: [bus]})

for bus_no in buses_dict.values():
    bus_no = bus_no[0]
    for index in buses_dict.keys():
        if index !=0:
            if index%int(bus_no) == 0:
                buses_dict[index].append(bus_no) 

def lcm(a, b):
    return abs(a*b) // math.gcd(a, b)
lcms={}
for key, value in buses_dict.items():
    if len(value)>1:
        add_on = lcm(int(value[0]), int(value[1]))
    else:
        add_on = int(value[0])
    lcms.update({key:add_on})

max_lcm = max(lcms.values())
for key, value in lcms.items():
    if value == max_lcm:
        key_max_lcm = key

print("max lcms", max_lcm, key_max_lcm)
print("lcms", lcms)
print("buses", buses_dict)

bus_number = 0
print(len(buses))
print(buses_dict)

current_time=max_lcm-key_max_lcm
counter = 1
#while counter<100:
while not sequence[len(sequence)-1]:
    current_time = max_lcm*counter - key_max_lcm
    iteration_time = current_time
    if counter%(1000000)==0:
        print(counter*0.0000000001*100)
        print(current_time+ key_max_lcm)
    counter+=1
    for key, value in lcms.items():
        current_time = iteration_time + key
        if current_time % value == 0:
            sequence[i] = True
            bus_number = value
            #print("true man")
        else:
            sequence = [False for j in sequence]
            break
    else:
        sequence[i] = True
        


print("The answer is: ", iteration_time)
print("Time: ", time.time()- real_start_time)
