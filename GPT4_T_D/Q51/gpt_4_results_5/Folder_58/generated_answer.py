
from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_dict = defaultdict(list)
    for word in strings:
        if len(word) >= 3:
            sorted_word = "".join(sorted(word.lower()))
            anagram_dict[sorted_word].append(word.lower())
    
    pairs_count = 0
    for v in anagram_dict.values():
        pairs_count += len(v) * (len(v) - 1) // 2
    
    if pairs_count > 60:
        return False
    return True
