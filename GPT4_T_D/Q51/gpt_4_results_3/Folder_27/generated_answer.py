
from collections import Counter

def if_contains_anagrams(lst):
    word_counts = Counter()
    for word in lst:
        word_counts[''.join(sorted(word.lower()))] += 1
    pairs = sum((count * (count - 1)) // 2 for count in word_counts.values() if len(word) >= 3)
    return pairs <= 113
