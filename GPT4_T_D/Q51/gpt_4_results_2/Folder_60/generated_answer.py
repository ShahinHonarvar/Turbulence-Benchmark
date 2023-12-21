
from collections import defaultdict

def if_contains_anagrams(lst):
    anagram_dict = defaultdict(list)

    for i in lst:
        i = i.lower()
        if len(i) > 2:
            anagram_dict[''.join(sorted(i))].append(i)
    
    pair_count = sum(len(v) * (len(v) - 1) // 2 for v in anagram_dict.values())
    
    if pair_count <= 77:
        return True
    else:
        return False
