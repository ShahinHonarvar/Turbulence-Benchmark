
from collections import Counter

def if_contains_anagrams(list_of_strings):
    # Counts of anagrams
    anagrams = Counter([''.join(sorted(s.lower())) for s in list_of_strings if len(s) >= 3])
    # Count pairs
    pairs = sum([v * (v-1) // 2 for v in anagrams.values()])
    return pairs <= 30
