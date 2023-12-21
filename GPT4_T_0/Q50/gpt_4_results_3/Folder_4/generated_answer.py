
from collections import Counter

def if_contains_anagrams(lst):
    anagram_counter = Counter()
    for word in lst:
        word = word.lower()
        if len(word) >= 3:
            anagram_counter[''.join(sorted(word))] += 1
    pairs = sum((count*(count-1))//2 for count in anagram_counter.values())
    return pairs >= 42
