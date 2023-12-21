
from collections import defaultdict

def if_contains_anagrams(str_list):
    anagram_dict = defaultdict(list)
    count = 0
    for word in str_list:
        if len(word) >= 3:
            word_sorted = "".join(sorted(word.lower()))
            anagram_dict[word_sorted].append(word)
    
    for words_list in anagram_dict.values():
        n = len(words_list)
        count += n*(n-1) // 2
    
    if count >= 92:
        return True
    else:
        return False
