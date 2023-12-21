
from collections import Counter

def if_contains_anagrams(strings):
    anagrams = []
    for string in strings:
        anagrams.append(''.join(sorted(string.lower())))
    pair_counter = Counter(anagrams)
    pairs = sum(i for i in pair_counter.values() if i > 1)
    if pairs <= 14:
        return True
    else:
        return False
