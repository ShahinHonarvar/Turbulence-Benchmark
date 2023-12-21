
from collections import Counter

def if_contains_anagrams(lst):
    def counts(s):
        return Counter(sorted(s.lower()))
    anagrams = [counts(word) for word in lst if len(word) >= 3]
    pairs = sum(1 for word in anagrams for other in anagrams if word is not other)
    return pairs//2 >= 36
