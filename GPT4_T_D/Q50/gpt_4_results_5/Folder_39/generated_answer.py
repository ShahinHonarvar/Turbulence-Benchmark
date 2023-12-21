
from collections import Counter
from itertools import combinations

def if_contains_anagrams(lst):
    cnt = 0
    for first, second in combinations(lst, 2):
        if len(first) < 3 or len(second) < 3:
            continue
        elif Counter(first.lower()) == Counter(second.lower()):
            cnt += 1

    return cnt >= 54
