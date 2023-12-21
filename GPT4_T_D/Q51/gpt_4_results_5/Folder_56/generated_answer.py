
from collections import Counter

def if_contains_anagrams(words):
    freq = Counter()
    for word in words:
        word = word.lower()
        if len(word) >= 3:
            freq[''.join(sorted(word))] += 1
    return len([count for count in freq.values() if count > 1]) <= 22
