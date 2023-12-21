
from collections import Counter

def if_contains_anagrams(strings):
    sorted_strings = [''.join(sorted(s.lower())) for s in strings if len(s) >= 3]
    count = Counter(sorted_strings)
    anagram_groups = [val for val in count.values() if val > 1]

    pairs = 0
    for group in anagram_groups:
        pairs += group * (group - 1) / 2

    return pairs <= 210
