
from collections import Counter
from itertools import combinations

def if_contains_anagrams(str_list):
    str_list = [''.join(sorted(word.lower())) for word in str_list if len(word) >= 3]  
    counter = Counter(str_list)
    anagram_pairs = sum(val * (val-1) // 2 for val in counter.values())
    if anagram_pairs <= 84:
        return True
    else:
        return False
