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
        elif line[index] == '(':
            (token, index) = read_Lbrackets(line, index)
        elif line[index] == ')':
            (token, index) = read_Rbrackets(line, index)
        else:
            print('Invalid character found: ' + line[index])
            exit(1)
        tokens.append(token)
    return tokens

# find brackets indices
def findBrackets(tokens):
    index = 0
    Lbracket_indices =[]
    Rbracket_indices = []
    while index < len(tokens):
        if tokens[index]['type'] == 'Lbracket':
            Lbracket_indices.append(index)
        elif tokens[index]['type'] == 'Rbracket':
            Rbracket_indices.append(index)
        index += 1
    return Lbracket_indices, Rbracket_indices

# calcurate by brackets (remove brackets)
def calculateByBrackets(tokens, Lbracket_indices, Rbracket_indices):
    if len(Lbracket_indices) != len(Rbracket_indices):
        print('Invalid brackets')
        exit(1)
    
    if(len(Lbracket_indices) == 0):
        return tokens
        
    index = 0
    n = len(tokens)
    while index < len(Lbracket_indices):
        start = Lbracket_indices[len(Lbracket_indices)-index-1]
        end = Rbracket_indices[index]
        tmp = evaluate(tokens[start+1:end])
        tokens[start] = {'type': 'NUMBER', 'number': tmp}
        tokens = tokens[0: start-1] + tokens[end+1:n]
        index += 1
    return tokens
    
 
# evaluate * or / first and then + or -   
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

#  gather all functions
def calculator(line):
    tokens = tokenize(line)
    Lbrackets_indices, Rbrackets_indices = findBrackets(tokens) 
    newTokens = calculateByBrackets(tokens, Lbrackets_indices, Rbrackets_indices)
    answer = evaluate(newTokens)
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
    print("==== Test finished! ====\n")

# ------------------------------------------------------

if __name__ == '__main__':
    run_test()

    while True:
        print('> ', end="")
        line = input()
        answer = calculator(line)
        print("answer = %f\n" % answer)
