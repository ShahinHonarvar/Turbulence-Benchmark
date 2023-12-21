
from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_dict = defaultdict(set)
    
    for string in strings:
        string_lower = string.lower()
        if len(string_lower) >= 3:
            sorted_string = "".join(sorted(string_lower))
            anagram_dict[sorted_string].add(string_lower)
            
    pair_count = 0
    for anagram_set in anagram_dict.values():
        if len(anagram_set) > 1:
            pair_count += len(anagram_set)*(len(anagram_set) - 1) / 2
            
    return pair_count >= 276
