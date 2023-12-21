
import itertools
from collections import Counter

def if_contains_anagrams(lst):
    def is_anagram(a, b):
        return len(a) >= 3 and Counter(a.lower()) == Counter(b.lower())

    pairs = list(itertools.combinations(lst, 2))
    count = sum(1 for a, b in pairs if is_anagram(a, b))

    return count >= 57
