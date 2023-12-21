
from collections import defaultdict

def count_pairs(strings):
    count = defaultdict(int)
    for s in strings:
        count[str(sorted(s.lower()))] += 1
    return sum(v * (v - 1) // 2 for v in count.values())

def if_contains_anagrams(strings):
    strings = [s for s in strings if len(s) >= 3 and s.isalpha()]
    return count_pairs(strings) <= 210
