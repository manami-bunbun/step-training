from collections import defaultdict
from pathlib import Path

def sortDictionary(filePath):
    new_dic = defaultdict(list) 
    
    with open(filePath) as f:
        lines = f.readlines()
        for l in lines:
            original_word = l.rstrip("\n")
            sorted_word = "".join(sorted(original_word))
            new_dic[sorted_word].append(original_word)
                
                
    sorted_dic = dict(sorted(new_dic.items())) 
    return sorted_dic


def findKeyByBinarySearch(sorted_targetWord, sorted_dic):
    
    keys = list(sorted_dic.keys())
    right = len(keys) -1
    left = 0
    
    while(left <= right):
        mid = left + (right-left)//2
        if keys[mid] == sorted_targetWord:
            return sorted_dic[keys[mid]]
        
        elif keys[mid] < sorted_targetWord:
            left = mid + 1
        else :
            right = mid - 1 
    
 
    return []
   
def solveTask1(targetWord):
        
    # 現在ディレクトリのパスを取得
    current_dir_path = Path(__file__).resolve().parent

    # words.txt
    words_path = current_dir_path / Path('../txt_files/words.txt')

    # sort dictionary
    sorted_dic = sortDictionary(words_path)
    
    # input
    sorted_targetWord = "".join(sorted(targetWord))
    
    # binary search 
    value = findKeyByBinarySearch(sorted_targetWord, sorted_dic)
    
    if len(value) > 0:
        return "The word can be anagram of "+ str(value)
    else:
        return "Anagram Not Found"
    
    


if __name__ == "__main__":
  
    # for normal use
    # targetWord = input("英数字を入力してください: ")
    # print(solveTask1(targetWord))
    
    # for tests
    print("test1:" + solveTask1(str('a'*10000000)))
    print("test2:" + solveTask1("!@#$%^&*()"))
    print("test3:" + solveTask1(""))
    print("test4:" + solveTask1(" "))
    print("test5:" + solveTask1("alepp"))
    
    
   
