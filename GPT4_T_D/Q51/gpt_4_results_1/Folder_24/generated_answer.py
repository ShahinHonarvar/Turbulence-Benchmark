
from collections import defaultdict

def if_contains_anagrams(strings):
    counter = defaultdict(int)
    for word in strings:
        counter[''.join(sorted(word.lower()))] += 1

    pairs = 0
    for count in counter.values():
        if len([c for c in counter if len(c) >= 3]) <= 96:
            pairs += count * (count - 1) // 2

    return pairs <= 96
