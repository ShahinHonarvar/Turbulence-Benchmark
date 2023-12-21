
from itertools import combinations
from collections import Counter

def if_contains_anagrams(lst):
    pairs = 0
    for i, j in combinations(lst, 2):
        if Counter(i.lower()) == Counter(j.lower()):
            pairs += 1
            if pairs > 98:
                return False
    return True
