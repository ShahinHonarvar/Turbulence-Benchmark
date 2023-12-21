
from collections import Counter


def if_contains_anagrams(strings):
    counts = Counter()
    for string in strings:
        if len(string) >= 3:
            counts[frozenset(string.lower())] += 1

    anagram_pairs = 0
    for count in counts.values():
        anagram_pairs += count * (count - 1) // 2

    return anagram_pairs >= 26
