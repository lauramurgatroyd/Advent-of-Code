import numpy as np
tree_layout = []
for line in open('day8.txt'):
    line = line.strip('\n')
    row = [int(i) for i in line]
    tree_layout.append(row)

print(tree_layout)
tree_layout = np.array(tree_layout)

visible_total = 2*(np.shape(tree_layout)[0]+np.shape(tree_layout)[1]) - 4

print("edge: ", visible_total)

print(np.shape(tree_layout)[0], np.shape(tree_layout)[1])
trees_counted = 0
for i in range(1, np.shape(tree_layout)[0]-1):
    for j in range(1, np.shape(tree_layout)[1]-1):
        trees_counted+=1
        # x = i and y = j

        current_tree = tree_layout[i][j]

        left = tree_layout[i, 0:j]
        right = tree_layout[i, j+1:np.shape(tree_layout)[1]]
        above = tree_layout[0:i, j]
        #print(tree_layout[i+1:np.shape(tree_layout)[0]+1])

        below = tree_layout[i+1:np.shape(tree_layout)[0], j]
        #print(type(above), type(below), type(left), type(right))

        

        for blocking_trees in [below, above, left, right]:
            if not isinstance(blocking_trees, np.ndarray):
                blocking_trees = [blocking_trees]
            visible = False
            for item in blocking_trees:
                if item >= current_tree:
                    visible = False
                    break
                else:
                    visible = True
            if visible:
                #print("This is visible: ", current_tree, "at", i, j)
                visible_total+=1
                break
print("the answer: ", visible_total)


print("Part 2 ---------------------")

visible_total = 2*(np.shape(tree_layout)[0]+np.shape(tree_layout)[1]) - 4

print("edge: ", visible_total)

print(np.shape(tree_layout)[0], np.shape(tree_layout)[1])
trees_counted = 0
highest_total = 0
for i in range(1, np.shape(tree_layout)[0]-1):
    for j in range(1, np.shape(tree_layout)[1]-1):
        trees_counted+=1
        # x = i and y = j

        current_tree = tree_layout[i][j]

        left = np.flip(tree_layout[i, 0:j])
        right = tree_layout[i, j+1:np.shape(tree_layout)[1]]
        above = np.flip(tree_layout[0:i, j])
        #print(tree_layout[i+1:np.shape(tree_layout)[0]+1])

        below = tree_layout[i+1:np.shape(tree_layout)[0], j]
        #print(type(above), type(below), type(left), type(right))

        current_tree_total = 1

        for blocking_trees in [below, above, left, right]:
            current_direction_total = 0
            if not isinstance(blocking_trees, np.ndarray):
                blocking_trees = [blocking_trees]
            visible = False
            for item in blocking_trees:
                current_direction_total += 1
                if item >= current_tree:
                    break
                    
            current_tree_total*=current_direction_total
        if current_tree_total > highest_total:
            highest_total = current_tree_total
print("the answer: ", highest_total)
