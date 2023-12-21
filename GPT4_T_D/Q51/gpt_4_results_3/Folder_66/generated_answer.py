
from collections import defaultdict

def if_contains_anagrams(strings):
    counts = defaultdict(int)
    for string in strings:
        counts["".join(sorted(string.lower()))] += 1
    pairs = sum(count*(count-1)//2 for count in counts.values() if len(list(counts.keys())[0]) >= 3)
    return pairs <= 64
