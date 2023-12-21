
from collections import Counter
from itertools import combinations

def count_anagrams(ls):
    count = 0
    for pair in combinations(ls,2):
        if len(pair[0]) >= 3 and len(pair[1]) >= 3:
            if Counter(pair[0].lower()) == Counter(pair[1].lower()):
                count += 1
    return count

def if_contains_anagrams(ls):
    return count_anagrams(ls) <= 89
