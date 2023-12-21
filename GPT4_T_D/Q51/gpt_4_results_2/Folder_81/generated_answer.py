
from collections import defaultdict
from itertools import combinations

def if_contains_anagrams(lst):
    count_dict = defaultdict(list)
    for word in lst:
        if len(word) >= 3:
            count_dict[''.join(sorted(word.lower()))].append(word)
    
    anagram_pairs = 0
    for words in count_dict.values():
        if len(words) > 1:
            anagram_pairs += len(list(combinations(words, 2)))
            if anagram_pairs > 79:
                return False
    return True
