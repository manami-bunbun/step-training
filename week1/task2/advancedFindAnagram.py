from collections import Counter
from pathlib import Path


# word.txt -> sort tupples[("abc", (Counter(word)))] -----------------
def makeDictionary(filePath):    
    count_list = []
    
    with open(filePath) as f:
        lines = f.readlines()
        for l in lines:
            original_word = l.rstrip("\n")
            count_list.append((original_word, Counter(original_word)))       
    count_list = sorted(count_list, key=lambda x: len(x[0]), reverse=True)
    count_list = sorted(count_list, key=lambda x: calculateOneWordScore(x[1]), reverse=True)
       
    return count_list


def calculateOneWordScore(oneWord):
    SCORES = [1, 3, 2, 2, 1, 3, 3, 1, 1, 4, 4, 2, 2, 1, 1, 3, 4, 1, 1, 1, 2, 3, 3, 4, 3, 4]    
    score = sum(SCORES[ord(char) - ord('a')] for char in oneWord)
    return score

# --------------------------------------------------------------

# small.txt -> dictionary
def countCharacter(filePath):
    target_dic = {}
    
    with open(filePath) as f:
        lines = f.readlines()
        for l in lines:
            original_word = l.rstrip("\n")
            target_dic[original_word] = Counter(original_word)
    return target_dic


# ------------------------------------------------------------

# find a highest score from sorted tupples
def is_subset(A, count_list):
    for word, hashmap in count_list:
        is_subset = all(A[char] >= hashmap[char] for char in hashmap)
        if is_subset:
            return word
    

# --------------------------------------------------------------



def solveTask2(inputFilename, outputFilename):
    # 現在ディレクトリのパスを取得
    current_dir_path = Path(__file__).resolve().parent

    # words.txt
    words_path = current_dir_path / Path('../txt_files/words.txt')

    # sort dictionary
    count_list = makeDictionary(words_path)
    
    input_path = current_dir_path / Path('../txt_files/') / inputFilename

    # output.txt (small_answer.txt)
    output_path = current_dir_path / Path('../txt_files/') / outputFilename

    # input
    target_dic = countCharacter(input_path)
    
    with open(output_path,'w') as f_ans:
        # compare hashmap to find valid word patterns
        for i in target_dic.values():
            f_ans.write(is_subset(i, count_list)+"\n")
    return


if __name__ == "__main__":
    solveTask2("small.txt", "small_answer.txt")
    print("Done small")
    solveTask2("medium.txt", "medium_answer.txt")
    print("Done medium")
    solveTask2("large.txt", "large_answer.txt")
    print("Done large")
