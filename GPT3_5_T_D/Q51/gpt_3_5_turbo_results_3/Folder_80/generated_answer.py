
from collections import Counter

def if_contains_anagrams(strings):
    anagram_counts = Counter()
    for string in strings:
        if len(string) < 3:
            continue
        normalized_string = string.lower()
        anagram_counts[normalized_string] += 1

    total_anagram_pairs = sum(count * (count - 1) // 2 for count in anagram_counts.values())
    return total_anagram_pairs <= 255
