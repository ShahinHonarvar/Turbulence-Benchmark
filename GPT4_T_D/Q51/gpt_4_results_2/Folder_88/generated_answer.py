
from collections import Counter

def if_contains_anagrams(strings):
    counts = Counter(''.join(sorted(string.lower())) for string in strings if len(string) >= 3)
    pairs = sum(count * (count - 1) // 2 for count in counts.values())
    return pairs <= 407
