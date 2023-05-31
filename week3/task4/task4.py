#! /usr/bin/python3

def remove_spaces(string):
    return string.replace(" ", "")

def read_number(line, index, minus=False):
    number = 0
    if minus:
        index +=1
    while index < len(line) and line[index].isdigit():
        number = number * 10 + int(line[index])
        index += 1
    if index < len(line) and line[index] == '.':
        index += 1
        decimal = 0.1
        while index < len(line) and line[index].isdigit():
            number += int(line[index]) * decimal
            decimal /= 10
            index += 1
    if minus:
        number *= -1
    token = {'type': 'NUMBER', 'number': number}
    return token, index


def read_plus(line, index):
    token = {'type': 'PLUS'}
    return token, index + 1


def read_minus(line, index):
    token = {'type': 'MINUS'}
    return token, index + 1


def read_multiple(line, index):
    token = {'type': 'MULTIPLE'}
    return token, index + 1


def read_devide(line, index):
    token = {'type': 'DEVIDE'}
    return token, index + 1

def read_Rbrackets(line, index):
    token = {'type': 'Rbrackets'}
    return token, index + 1

def read_Lbrackets(line, index):
    token = {'type': 'Lbrackets'}
    return token, index + 1

def read_abs(line, index):
    if line[index:index+3] != 'abs':
        print('Invalid syntax')
        exit(1)
    token = {'type': 'ABS'}
    return token, index + 3

def read_int(line, index):
    if line[index:index+3] != 'int':
        print('Invalid syntax')
        exit(1)
    token = {'type': 'INT'}
    return token, index + 3

def read_round(line, index):
    if line[index:index+5] != 'round':
        print('Invalid syntax')
        exit(1)
    token = {'type': 'ROUND'}
    return token, index + 5

    
def tokenize(line):
    tokens = []
    index = 0
    while index < len(line):
        if line[index].isdigit():
            (token, index) = read_number(line, index)
        elif line[index] == '+':
            (token, index) = read_plus(line, index)
        elif line[index] == '-' and line[index-1]=='(':
            (token, index) = read_number(line, index, minus=True)
        elif line[index] == '-':
            (token, index) = read_minus(line, index)
        elif line[index] == '*':
            (token, index) = read_multiple(line, index)
        elif line[index] == '/':
            (token, index) = read_devide(line, index)
        elif line[index] == '(':
            (token, index) = read_Lbrackets(line, index)
        elif line[index] == ')':
            (token, index) = read_Rbrackets(line, index)
        elif line[index] == 'a':
            (token, index) = read_abs(line, index)
        elif line[index] == 'i':
            (token, index) = read_int(line, index)
        elif line[index] == 'r':
            (token, index) = read_round(line, index)    
        else:
            print('Invalid character found: ' + line[index])
            exit(1)
        tokens.append(token)
    return tokens


# calcurate by brackets (remove brackets)
def calculateInsideBrackets(tokens):
    index = 0
    stack = []
    while index < len(tokens):
        if tokens[index]['type'] == 'Rbrackets':
            inside_brackets =[]
            while stack[-1]['type'] != 'Lbrackets':
                inside_brackets = [stack.pop()] + inside_brackets
            stack.pop() # remove '('
            withoutBrackets = evaluate(inside_brackets)
            #最初にabsやintやroundがあったら計算できるように
            while len(stack)>0 and (stack[-1]['type'] == 'ABS' or stack[-1]['type'] == 'INT' or stack[-1]['type'] == 'ROUND'):
                operation = stack.pop()['type']
                withoutBrackets = calculateByAbsIntRound(withoutBrackets, operation)
            stack.append({'type': 'NUMBER', 'number': withoutBrackets})
        else:
            stack.append(tokens[index])
        index += 1
    return stack

# calculate by abs or int or round
def calculateByAbsIntRound(withoutBrackets, type):
    if type == 'ABS':
        return abs(withoutBrackets)
    elif type == 'INT':
        return int(withoutBrackets)
    elif type == 'ROUND':
        return round(withoutBrackets)
    else:
        print('Invalid syntax')
        exit(1)
 
# evaluate * or / first and then + or -   
def evaluate(tokens):
    if (len(tokens) == 1):
        return tokens[0]['number']
        
    # evaluate * or /　(記号を中心にその左右の数字を計算するか判断)
    tokens.insert(0, {'type': 'PLUS'}) # Insert a dummy '+' token
    
    # 最初の数字を一時保存する
    p = 1
    while tokens[p]['type']!="NUMBER":
        p+=1        
    tmp = tokens[p]['number'] 
    
    index = 2
    newTokens = [{'type': 'PLUS'}]
    while index < len(tokens):
        if tokens[index]['type'] == 'PLUS' or tokens[index]['type'] == 'MINUS':
            newTokens.append( {'type': 'NUMBER', 'number': tmp})
            newTokens.append(tokens[index])
            tmp = tokens[index+1]['number']
        elif tokens[index]['type'] == 'MULTIPLE':
            tmp *= tokens[index+1]['number']
        elif tokens[index]['type'] == 'DEVIDE':
            if tokens[index+1]['number'] == 0:
                print('-----------ZeroDivisionError------------')
                print('Wanna know why? see https://en.wikipedia.org/wiki/Division_by_zero')
                exit(1)
            tmp /= tokens[index+1]['number']    
        elif tokens[index]['type'] == 'NUMBER':
            pass
        else:
            print('Invalid syntax:' + str(tokens[index]))
            exit(1)
        index += 2
    newTokens.append( {'type': 'NUMBER', 'number': tmp})

    # evaluate + or -　(数字中心)
    answer = 0
    index = 1
    while index < len(newTokens):
        if newTokens[index]['type'] == 'NUMBER':
            if newTokens[index - 1]['type'] == 'PLUS':
                answer += newTokens[index]['number']
            elif newTokens[index - 1]['type'] == 'MINUS':
                answer -= newTokens[index]['number']
            else:
                print('Invalid syntax')
                exit(1)
        index += 1
    return answer

#  gather all functions
def calculator(line):
    lineWithoutSpaces=remove_spaces(line)
    tokens = tokenize(lineWithoutSpaces)
    tokensWithoutBrackets = calculateInsideBrackets(tokens)
    answer = evaluate(tokensWithoutBrackets)
    return answer

# ------------------------test------------------------

def test(line):
    actual_answer = calculator(line)
    expected_answer = eval(line)
    if abs(actual_answer - expected_answer) < 1e-8:
        print("PASS! (%s = %f)" % (line, expected_answer))
    else:
        print("FAIL! (%s should be %f but was %f)" % (line, expected_answer, actual_answer))


# Add more tests to this function :)
def run_test():
    print("==== Test started! ====")
    test("1+2")
    test("1.0+2.1-3")
    test("1+2*3+1")
    test("1.0+2.1/3+1")
    test("abs(-5)")  
    test("int(3.8)")  
    test("round(3.14159)") 
    test("abs((1.0)+(2.1))/3+1")
    test("int(abs((1.0)+(2.1))/3)+1")
    test("3*abs(4)+int(5.6)/round(2.3)") 
    test("(2+int(3.7))*round(1.8+0.2)-abs(4.5)")
    test("4/0") 
    print("==== Test finished! ====\n")

# ------------------------------------------------------

if __name__ == '__main__':
    run_test()

    while True:
        print('> ', end="")
        line = input()
        answer = calculator(line)
        print("answer = %f\n" % answer)
