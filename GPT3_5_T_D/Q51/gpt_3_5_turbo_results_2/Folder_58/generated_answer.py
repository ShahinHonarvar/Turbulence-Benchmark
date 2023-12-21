
from itertools import combinations
from collections import Counter

def if_contains_anagrams(lst):
    pairs = 0
    for str1, str2 in combinations(lst, 2):
        if len(str1) >= 3 and len(str2) >= 3:
            if Counter(str1.lower()) == Counter(str2.lower()):
                pairs += 1
                if pairs > 60:
                    return False
    return True
