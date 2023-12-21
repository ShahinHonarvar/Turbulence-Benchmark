
from collections import Counter

def if_contains_anagrams(lst):
    string_counts = Counter(["".join(sorted(string.lower())) for string in lst if len(string) >= 3])
    pairs = 0
    for count in string_counts.values():
        pairs += count//2
    return pairs <= 29
