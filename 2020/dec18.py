
import re

questions = []
with open("Puzzle18_Input.txt") as input_file:
    for line in input_file:
        # questions.append(l.strip('\n'))
        line = line.strip('\n')
        #match_iterator = re.finditer(r'\(([^\)]+)\)', line)
        #match_iterator = re.finditer(r'.*\(.*', line)
        expressions = []
        ranges = []
        expression = line
        while '(' in expression and len(expression)>1:
            start = None
            stop = None
            brackets_count = None
            print(expression)
            for i, char in enumerate(expression):
                #print(i, char)
                if brackets_count is None:
                    if char == '(':
                        #print("add 1 ")
                        start = i+1
                        brackets_count = 1
                elif char == '(':
                    brackets_count += 1
                elif char == ')':
                    brackets_count -= 1
                    stop = i
                #print(brackets_count)
                if brackets_count ==0:
                    break
            index_range = [start, stop]
            #expression = line[0: start:] + line[stop + 1::]
            sub_expression = expression[start:stop]
            print("sub", sub_expression)
            if '(' not  in sub_expression:

                sub_range = []
                sub_expression = sub_expression.strip(' ').split()
                total = int(sub_expression[0])
                for i, char in enumerate(sub_expression):
                    if char in ['*', '/', '+', '-']:
                        if char == '*':
                            total *= int(sub_expression[i+1])
                        if char == '/':
                            total = total/int(sub_expression[i+1])
                        if char == '+':
                            total += int(sub_expression[i+1])
                        if char == '-':
                            total
                            total -= int(sub_expression[i+1])
                sub_expression = total
                print("total: ", total)

                expression = expression.replace(expression[start-1:stop+1], str(sub_expression))
                print(" Expression: ", expression)
                #print("replace the: ", )
                if '(' not in expression:
                    expressions.append(expression)
                    ranges.append(index_range)
            else:
                expressions.append(expression)
                expression = expression[start:stop]
                ranges.append(index_range)
            print(" Expression: ", expression)

            #expressions.append(expression)
            
        print("exp", expressions)
        print("ranges", ranges)
        expressions.reverse()
        ranges.reverse()
        for i, exp in enumerate(expressions):
            if i != len(expressions)-1:
                start = ranges[i+1][0]
                stop = ranges[i+1][1]
                expressions[i+1] = expressions[i+1].replace(expressions[i+1][start-1:stop+1], str(expressions[i]))

        print("exp",expressions)
        print("ranges",ranges)
        print(expressions[-1]) # this here is the correct exp to then evaluate for ((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2
        # start = ranges[-1][0]
        # stop = ranges[-1][1]
        # line = line.replace(line[start-1:stop+1], str(expressions[-1]))

            # print(expression)
            # print(expression[0])

        # for match in match_iterator:
        #     index_range = [match.start(0), match.end(0)]
        #     options = match.group(1)
        #     print(options)
            # # keyword is last word in previous substring:
            # keyword_string = line[:match.start(0)]
            # keyword_match_iter = [k for k in re.finditer(
            #     r'[^\,/\s]+', keyword_string) if k.group() != '=']
            # keyword = keyword_match_iter[-1].group().strip(' =')
            # index_range[0] = keyword_match_iter[-1].start()
            # params.update({keyword: options})
            # index_ranges.append(index_range)
