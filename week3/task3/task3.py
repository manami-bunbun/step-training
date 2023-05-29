#! /usr/bin/python3

def read_number(line, index):
    number = 0
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


def tokenize(line):
    tokens = []
    index = 0
    while index < len(line):
        if line[index].isdigit():
            (token, index) = read_number(line, index)
        elif line[index] == '+':
            (token, index) = read_plus(line, index)
        elif line[index] == '-':
            (token, index) = read_minus(line, index)
        elif line[index] == '*':
            (token, index) = read_multiple(line, index)
        elif line[index] == '/':
            (token, index) = read_devide(line, index)
        else:
            print('Invalid character found: ' + line[index])
            exit(1)
        tokens.append(token)
    return tokens


def evaluate(tokens):
    # evaluate * or /
    tokens.insert(0, {'type': 'PLUS'}) # Insert a dummy '+' token
    tmp = tokens[1]['number'] 
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
            tmp /= tokens[index+1]['number']    
        else:
            print('Invalid syntax')
            exit(1)
        index += 2
    newTokens.append( {'type': 'NUMBER', 'number': tmp})
    
    
    # evaluate + or -
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


def test(line):
    tokens = tokenize(line)
    actual_answer = evaluate(tokens)
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
    print("==== Test finished! ====\n")

run_test()

while True:
    print('> ', end="")
    line = input()
    tokens = tokenize(line)
    answer = evaluate(tokens)
    print("answer = %f\n" % answer)
