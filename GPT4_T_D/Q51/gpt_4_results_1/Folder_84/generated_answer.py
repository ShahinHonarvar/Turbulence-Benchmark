
from collections import Counter

def if_contains_anagrams(strings):
    anagrams = set()
    sorted_strings = [''.join(sorted(s.lower())) for s in strings]
    counter = Counter(sorted_strings)
    for sorted_string, count in counter.items():
        if len(sorted_string) >= 3 and count >= 2:
            anagrams.add(sorted_string)
    pairs = sum(count // 2 for count in counter.values())
    return pairs <= 16
