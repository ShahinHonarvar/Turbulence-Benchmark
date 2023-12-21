
import itertools
from collections import Counter

def is_anagram(s1, s2):
    return Counter(s1) == Counter(s2)

def if_contains_anagrams(lst):
    anagram_pairs = 0
    for pair in itertools.combinations(lst, 2):
        s1, s2 = pair[0].lower(), pair[1].lower()
        if len(s1) >= 3 and len(s2) >= 3 and is_anagram(s1, s2):
            anagram_pairs += 1
            
    return anagram_pairs <= 113
