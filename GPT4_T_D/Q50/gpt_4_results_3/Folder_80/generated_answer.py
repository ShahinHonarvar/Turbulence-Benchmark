
from collections import Counter

def if_contains_anagrams(str_list):
    str_list = [''.join(sorted(s.lower())) for s in str_list if len(s) >= 3]
    str_count = Counter(str_list)
    anagram_pairs = sum(v * (v - 1) // 2 for v in str_count.values())
    if anagram_pairs >= 19:
        return True
    else:
        return False
