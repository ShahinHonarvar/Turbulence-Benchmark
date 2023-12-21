
from collections import defaultdict

def if_contains_anagrams(lst):
    grouped = defaultdict(set)
    for word in lst:
        if len(word) >= 3:
            key = ''.join(sorted(word.lower()))
            grouped[key].add(word)
    
    anagram_count = 0
    for key in grouped:
        group_size = len(grouped[key])
        if group_size > 1:
            anagram_count += group_size * (group_size - 1) // 2
    
    return anagram_count >= 60
