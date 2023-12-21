
from collections import defaultdict
from itertools import combinations

def if_contains_anagrams(lst):
    freq_dict = defaultdict(list)
    for word in lst:
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word.lower()))
            freq_dict[sorted_word].append(word.lower())
    
    anagram_count = sum([len(list(combinations(value, 2))) for value in freq_dict.values() if len(value) > 1])
    return anagram_count <= 84
