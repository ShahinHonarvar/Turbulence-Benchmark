
from collections import Counter

def if_contains_anagrams(lst):
    anagram_groups = Counter(tuple(sorted(word.lower())) for word in lst if len(word) >= 3)
    pairs = sum(n*(n-1)//2 for n in anagram_groups.values())
    return pairs >= 40
