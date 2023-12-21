
from itertools import combinations
from collections import Counter

def if_contains_anagrams(strings):
    count = 0
    for s1, s2 in combinations(strings, 2):
        if len(s1) >= 3 and Counter(s1.lower()) == Counter(s2.lower()):
            count += 1
            if count >= 89:
                return True
    return False
