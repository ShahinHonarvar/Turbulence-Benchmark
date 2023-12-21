
from collections import defaultdict

def if_contains_anagrams(lst):
    def is_anagram(str1, str2):
        return sorted(str1) == sorted(str2)
    
    met_dict = defaultdict(list)
    
    for word in lst:
        met_dict[''.join(sorted(word.lower()))].append(word)
    
    anagram_pairs = [val for val in met_dict.values() if len(val) > 1]
    
    pair_count = 0
    for pair in anagram_pairs:
        if len(pair[0]) >= 3:
            pair_count += 1
    
    if pair_count <= 39:
        return True
    else:
        return False
