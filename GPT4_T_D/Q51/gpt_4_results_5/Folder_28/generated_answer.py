
from collections import defaultdict

def if_contains_anagrams(lst):
    anagram_dict = defaultdict(list)
    
    for s in lst:
        if len(s) >= 3:
            sorted_string = ''.join(sorted(s.lower()))
            anagram_dict[sorted_string].append(s)

    anagram_pairs = 0
    for k, v in anagram_dict.items():
        if len(v) > 1:
            anagram_pairs += len(v) * (len(v) - 1) // 2
            
    return anagram_pairs <= 78
