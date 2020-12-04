import numpy as np

print("PUZZLE 1 --------------------------------------------------------")

passports=[]
lines = 0
current_passport={}
with open("Puzzle4_Input.txt") as input_file:
    for l in input_file:
        if l != '\n':
            l=l.strip('\n')
            l=l.split(" ")
            for i, val in enumerate(l):
                sep = val.split(":")
                l[i] =sep
            l=dict(l)
            current_passport.update(l)
            
        else:
            passports.append(current_passport)
            current_passport={}
    passports.append(current_passport)
    current_passport={}
fails=0
count = 0
p_len = len(passports)
for passport in passports:
    if passport == {}:
        passports.pop(count)
        p_len = p_len-1
    else:
        for key in ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']:
            if key not in passport:
                # print(passport)
                #print(count)
                fails+=1
                passport['fail']= True
                break       
        count+=1

successes= p_len-fails

print("Number of valid passports: ", successes)
# print(passports)

print("PUZZLE 2 --------------------------------------------------------")

from schema import Optional, Schema, SchemaError

for passport in passports:
    if 'fail' not in passport.keys():
        try:
            passport['byr'] = int(passport['byr'])
            if not (1919<passport['byr']<2003 and len(str(passport['byr']))==4):
                passport['fail'] = True
            passport['iyr'] = int(passport['iyr'])
            if not (2009<passport['iyr']<2021 and len(str(passport['iyr']))==4):
                passport['fail'] = True
            passport['eyr'] = int(passport['eyr'])
            if not (2019<passport['eyr']<2031 and len(str(passport['eyr']))==4):
                passport['fail'] = True
            
            passport['hgt'] = [int(passport['hgt'][:-2]),passport['hgt'][-2:]]
            if passport['hgt'][1] not in ['cm','in']:
                passport['fail'] = True
            elif passport['hgt'][1] =='cm':
                if not 149<passport['hgt'][0]<194:
                    passport['fail'] = True
            else:
                if not 58<passport['hgt'][0]<77:
                    passport['fail'] = True
            int(passport['hgt'][0])
            
            #TODO: hcl
            if not (passport['hcl'][0] == '#' and len(passport['hcl']) == 7):
                passport['fail'] = True
            for i in passport['hcl'][6:]:
                if i not in ['0', '1', '2', '3', '4', '5', '6', '7','8','9', 'a', 'b', 'c', 'd', 'e', 'f']:
                    passport['fail'] = True

            if passport['ecl'] not in  ['amb','blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
                passport['fail'] = True
            
            if not (len(passport['pid'])==9):# and str(passport['pid'])[:1]=='0'):
                passport['fail']=True
            for i in passport['pid']:
                int(i)
                #passport['fail']=True
        except Exception as e:
            #print(e)
            passport['fail'] = True


successes=0
for passport in passports:
    if 'fail' not in passport:
        successes+=1
        #print(passport)
print("Number of valid passports: ", successes)

#TODO: build a schema instead....

# PassportSchema = Schema({
# #    'byr': int,
# #    'iyr': int,
# #    'eyr': int,
#    #'hgt': len>3 then strip 2 chars
#    #'ecl': ['amb','blu', 'brn', 'gry', 'grn', 'hzl', 'oth'],
# #    'pid': int, # 9 digits, leading 0s

# })

# PassportSchema.validate(passports[1])

