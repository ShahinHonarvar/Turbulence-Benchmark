
from collections import defaultdict

def if_contains_anagrams(strings_list):
    canon_dict = defaultdict(list)
    for s in strings_list:
        if len(s) >= 3:
            canon_dict["".join(sorted(s.lower()))].append(s)
            
    anagram_pairs = sum(len(v) * (len(v) - 1) // 2 for v in canon_dict.values())
    
    return anagram_pairs >= 93
