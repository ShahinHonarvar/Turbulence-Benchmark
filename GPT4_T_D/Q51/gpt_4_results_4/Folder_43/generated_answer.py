
from collections import Counter

def if_contains_anagrams(list_of_strings):
    counts = Counter(''.join(sorted(string.lower())) for string in list_of_strings if len(string) >= 3)
    return sum(value >= 2 for value in counts.values()) <= 3
