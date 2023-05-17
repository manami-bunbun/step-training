from collections import Counter
from pathlib import Path

def makeDictionary(filePath):
    new_dic = {}
    count_dic = {}
    
    with open(filePath) as f:
        lines = f.readlines()
        for l in lines:
            original_word = l.rstrip("\n")
            sorted_word = "".join(sorted(original_word))
            if sorted_word in new_dic:
                new_dic[sorted_word].append(original_word)
            else:
                new_dic[sorted_word] = [ original_word ]
                count_dic[original_word] = Counter(original_word)   
    return new_dic, count_dic

def is_subset(A, count_dic):
    valid_lists = []
    for word, hashmap in count_dic.items():
        is_subset = all(A[char] >= hashmap[char] for char in hashmap)
        if is_subset:
            valid_lists.append(word)
    return valid_lists

def calculateScores(subsetAnagrams):
    SCORES = [1, 3, 2, 2, 1, 3, 3, 1, 1, 4, 4, 2, 2, 1, 1, 3, 4, 1, 1, 1, 2, 3, 3, 4, 3, 4]
    scores = []
    for anagram in subsetAnagrams:
        score = sum(SCORES[ord(char) - ord('a')] for char in anagram)
        scores.append((score, anagram))
    return max(scores)[1]

def countCharacter(filePath):
    target_dic = {}
    
    with open(filePath) as f:
        lines = f.readlines()
        for l in lines:
            original_word = l.rstrip("\n")
            target_dic[original_word] = Counter(original_word)
    return target_dic

def solveTask2(inputFilename, outputFilename):
    # 現在ディレクトリのパスを取得
    current_dir_path = Path(__file__).resolve().parent

    # words.txt
    words_path = current_dir_path / Path('../txt_files/words.txt')

    # sort dictionary
    sorted_dic, count_dic = makeDictionary(words_path)
    
    input_path = current_dir_path / Path('../txt_files/') / inputFilename

    # output.txt (small_answer.txt)
    output_path = current_dir_path / Path('../txt_files/') / outputFilename

    # input
    target_dic = countCharacter(input_path)

    # anagramCandidates
    all_valid_lists = []
    # compare hashmap to find valid word patterns
    for i in target_dic.values():
        all_valid_lists.append(is_subset(i, count_dic))
        
    with open(output_path,'w') as f_ans:
        for k in all_valid_lists:
            f_ans.write(calculateScores(k)+"\n")
    return


if __name__ == "__main__":
    solveTask2("small.txt", "small_answer.txt")
    print("Done small")
    solveTask2("medium.txt", "medium_answer.txt")
    print("Done medium")
    solveTask2("large.txt", "large_answer.txt")
    print("Done large")
