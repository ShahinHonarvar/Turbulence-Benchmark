
from collections import Counter

def if_contains_anagrams(lst):
    anagram_counter = 0
    str_lst = ["".join(sorted(s.lower())) for s in lst if len(s) >= 3]
    str_counts = Counter(str_lst)

    for val in str_counts.values():
        anagram_counter += val * (val - 1) // 2

    if anagram_counter >= 24:
        return True
    else:
        return False
