
import itertools
from collections import Counter

def if_contains_anagrams(strings):
    count = 0
    for s1, s2 in itertools.combinations(strings, 2):
        s1_lower = s1.lower()
        s2_lower = s2.lower()
        if s1_lower != s2_lower and sorted(s1_lower) == sorted(s2_lower) and len(s1_lower) >= 3:
            count += 1
            if count > 276:
                return False
    return True
