
def if_contains_anagrams(str_list):
    from collections import Counter
    def countAnagram(str_list): 
        wordDict = Counter(''.join(sorted(word.lower())) for word in str_list if len(word) >= 3) 
        return sum(sum(range(wordDict[word])) for word in wordDict.values() if wordDict[word] > 1)

    return countAnagram(str_list) <= 73
