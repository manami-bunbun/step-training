# week3


## task1 
> モジュール化されたプログラムを変更して、「*」「/」に対応しよう
> 例： 3.0 + 4 * 2 − 1 / 5
> 不正な入力はないと仮定してよい
> 細かい仕様は好きに定義してください

初めは*と/を別関数にしたが、計算は一つのモジュールに責任を取らせた方が良いと思って、

evaluate()にまとめた

```python
def evaluate(tokens):
    # evaluate * or /
    tokens.insert(0, {'type': 'PLUS'}) # Insert a dummy '+' token
    tmp = tokens[1]['number'] #最初の数字を保存
    index = 2
    newTokens = [{'type': 'PLUS'}]
    # 記号中心で判定
    while index < len(tokens):
        # + or - が出てきたら、その前の数字と記号を記録して、次の数字をtmpに代入
        if tokens[index]['type'] == 'PLUS' or tokens[index]['type'] == 'MINUS':
            newTokens.append( {'type': 'NUMBER', 'number': tmp}) 
            newTokens.append(tokens[index])
            tmp = tokens[index+1]['number']
        # * or / が出てきたら、tmpにその前後の数字の計算結果を代入
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
    newTokens.insert(0, {'type': 'PLUS'}) # Insert a dummy '+' token
    index = 1
    #数字中心で判定
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
```

## task2
> `run_test()`内にテストを追加



