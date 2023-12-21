
from collections import defaultdict
from itertools import combinations

def if_contains_anagrams(strings):
    counter = defaultdict(int)
    for string in strings:
        if len(string) < 3:
            continue
        key = ''.join(sorted(string.lower()))
        counter[key] += 1

    pairs = 0
    for value in counter.values():
        pairs += value * (value - 1) // 2

    return pairs <= 36
