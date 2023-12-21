
import itertools
from collections import Counter

def if_contains_anagrams(strings):
    count = 0
    for i, j in itertools.combinations(strings, 2):
        if len(i) >= 3 and len(j) >= 3:
            if Counter(i.lower()) == Counter(j.lower()):
                count += 1
        if count > 392:
            return False
    return True
