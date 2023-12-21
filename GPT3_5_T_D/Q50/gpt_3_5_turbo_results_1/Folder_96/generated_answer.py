
from collections import Counter

def if_contains_anagrams(strings):
    counter = Counter(s.lower() for s in strings if len(s) >= 3)
    anagram_count = sum(count // 2 for count in counter.values())
    return anagram_count >= 98
