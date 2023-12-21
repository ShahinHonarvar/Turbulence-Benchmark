
from collections import defaultdict
from itertools import combinations

def if_contains_anagrams(strings_list):
    anagram_dict = defaultdict(list)
    for word in strings_list:
        if len(word) >= 3:
            anagram_dict[''.join(sorted(word.lower()))].append(word)
    
    anagram_pairs = 0
    for key in anagram_dict:
        if len(anagram_dict[key]) >= 2:
            anagram_pairs += len(list(combinations(anagram_dict[key], 2)))
            
    return anagram_pairs >= 68
