
from itertools import combinations

def if_contains_anagrams(lst):
    def is_anagram(s1, s2):
        s1, s2 = s1.lower(), s2.lower()
        if len(set(s1)) < 3 or len(set(s2)) < 3:
            return False
        return sorted(s1) == sorted(s2)
    pairs = list(combinations(lst, 2))
    anagram_pairs = [pair for pair in pairs if is_anagram(*pair)]
    return len(anagram_pairs) <= 416
