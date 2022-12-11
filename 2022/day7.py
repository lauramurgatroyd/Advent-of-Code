# $ cd /
# $ ls
# dir a
# 14848514 b.txt
# 8504156 c.dat
# dir d
# $ cd a
# $ ls
# dir e
# 29116 f
# 2557 g
# 62596 h.lst
# $ cd e
# $ ls
# 584 i
# $ cd ..
# $ cd ..
# $ cd d
# $ ls
# 4060174 j
# 8033020 d.log
# 5626152 d.ext
# 7214296 k
files = {}
current_dir = None
ls_contents=False
previous_dirs = []

for line in open('day7.txt'):
    line = line.strip('\n')
    if '$' in line:
        line = line.replace("$ ", "")
        ls_contents=False
    else:
        ls_contents = True
    #print([line])
    if ls_contents:
        line = line.split(' ')
        print("ls content: ", line)
        if line[0] == 'dir':
            current_dir[line[1]] =  {}
        else:
            current_dir[line[1]] = line[0]


    elif 'cd' in line:
        line = line.replace("cd ", "").strip('\n')

        if line == '..':
            current_dir = previous_dirs.pop(-1)
        else:
            if current_dir is None:
                files[line] = {}
                current_dir = files[line]
            else:
                current_dir[line] = {}
                previous_dirs.append(current_dir)
                current_dir = current_dir[line]
                print("prev: ", previous_dirs[-1])
                print("curr: ", current_dir)
    elif line == 'ls':
        pass

    

        #print([line])
print(files)

totals = {}


for key, value in files:
    totals[key] = 0
    done = False
    current_dict = value
    while not done:
        try:
            int(value)
            totals[key]+=value
            done = True
        for key, value in value:
            

    



