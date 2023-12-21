
from collections import Counter

def if_contains_anagrams(lst):
    anagram_dict = {}
    for word in lst:
        word_lower = word.lower()
        if len(word_lower) >= 3:
            anagram_dict[''.join(sorted(word_lower))] += 1
    
    pairs_cnt = sum([value*(value-1)//2 for value in anagram_dict.values()])
    return pairs_cnt <= 85
