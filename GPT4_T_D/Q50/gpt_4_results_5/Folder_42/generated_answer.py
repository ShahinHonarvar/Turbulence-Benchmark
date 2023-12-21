
from itertools import combinations
from collections import Counter

def if_contains_anagrams(lst):
    pairs_count = 0
    for s1, s2 in combinations(lst, 2):
        s1 = s1.lower()
        s2 = s2.lower()
        if len(s1) < 3 or len(s2) < 3:
            continue
        if Counter(s1) == Counter(s2):
            pairs_count += 1
            if pairs_count >= 233:
                return True
    return False
