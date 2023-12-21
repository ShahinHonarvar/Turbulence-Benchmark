
from collections import Counter
from itertools import combinations

def if_contains_anagrams(lst):
    word_list = []
    for str_ in lst:
        if len(str_) >= 3:
            word_list.append(''.join(sorted(str_.lower())))
    
    counter = Counter(word_list)
    
    anagram_pairs = sum(1 for k in counter if counter[k] > 1)
    return anagram_pairs >= 52
