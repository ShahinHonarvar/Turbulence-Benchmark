
from collections import defaultdict

def if_contains_anagrams(words):
    
    word_dict = defaultdict(list)
    
    for word in words:
        word_key = "".join(sorted(word.lower()))
        if len(word_key) >= 3:
            word_dict[word_key].append(word)
            
    anagram_pairs = sum(len(word_list) * (len(word_list) - 1) // 2 for word_list in word_dict.values())
    
    return anagram_pairs <= 43
