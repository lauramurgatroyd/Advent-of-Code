import numpy as np
string = "a"
print(ord(string)-96)
string = "A"
print(ord(string)-65+27)
sum=0
with open('input3.txt') as input:
    for l in input:
        print(l)
        first_letters=[]
        num_items = len(l)
        print("items: ", num_items)
        for i, letter in enumerate(l):
            if i < np.floor(num_items/2):
                first_letters.append(letter)
            else:
                #print(first_letters)
                if letter in first_letters:
                    #print(letter)
                    print(first_letters)
                    if letter.lower() == letter:
                        sum+=ord(letter) - 96
                        break
                    else:
                        sum+=ord(letter)-65+27
                        break
                    print(letter, sum)


print(sum)

#-------------------------------2

print("puzzle 2")
sum=0
with open('input3.txt') as input:
    i=0
    current_bags = []
    for l in input:
        if i<2:
            current_bags.append(l)
            i+=1
        elif i==2:
            current_bags.append(l)
            common_items = [j for j in current_bags[0] if j in current_bags[1] and j in current_bags[2]]
            letter = common_items[0]
            print(letter)
            if letter.lower() == letter:
                sum+=ord(letter) - 96
            else:
                sum+=ord(letter)-65+27
            i=0
            current_bags = []

print(sum)
    