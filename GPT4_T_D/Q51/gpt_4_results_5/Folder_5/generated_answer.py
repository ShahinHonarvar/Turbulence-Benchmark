
from collections import defaultdict

def if_contains_anagrams(words):
    frequency = defaultdict(int)
    for word in words:
        word = word.lower()
        if len(word) >= 3:
            frequency[''.join(sorted(word))] += 1
    anagram_pairs = sum(v // 2 for v in frequency.values())
    return anagram_pairs <= 4
