
from itertools import combinations
from collections import Counter

def if_contains_anagrams(strings):
    count = 0
    for i, j in combinations(range(len(strings)), 2):
        if len(strings[i]) >= 3 and len(strings[j]) >= 3:
            if Counter(strings[i].lower()) == Counter(strings[j].lower()):
                count += 1
                if count > 407:
                    return False
    return True
