
from collections import Counter

def if_contains_anagrams(strings):
    strings = [string.lower() for string in strings if len(string) >= 3]
    sort_string = sorted([''.join(sorted(string)) for string in strings])
    counter = Counter(sort_string)
    pairs_count = 0
    for key, value in counter.items():
        pairs_count += value * (value - 1) / 2
    return pairs_count >=35
