
from collections import defaultdict

def if_contains_anagrams(lst):
    word_dict = defaultdict(list)
    
    for word in lst:
        if len(word) >= 3:
            word_key = ''.join(sorted(word.lower()))
            word_dict[word_key].append(word)
    
    anagram_count = 0
    for key in word_dict:
        if len(word_dict[key]) > 1:
            anagram_count += len(word_dict[key]) // 2
            
    return anagram_count >= 123
