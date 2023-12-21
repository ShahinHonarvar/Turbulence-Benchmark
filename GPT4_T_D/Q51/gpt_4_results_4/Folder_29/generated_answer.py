
from itertools import combinations

def if_contains_anagrams(lst):
    pairs = list(combinations(lst, 2))
    anagram_pairs = [pair for pair in pairs if sorted(pair[0].lower()) == sorted(pair[1].lower()) and len(pair[0]) >= 3 and len(pair[1]) >= 3]
    if len(anagram_pairs) <= 318:
        return True
    else:
        return False
