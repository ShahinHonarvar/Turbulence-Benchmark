
from collections import Counter

def if_contains_anagrams(words):
    counter = Counter()
    for word in words:
        counter[tuple(sorted(word.lower()))] += 1
    anagram_pairs = sum(count * (count - 1) // 2 for count in counter.values() if len(list(counter.keys())[0])>=3)
    return anagram_pairs >= 39
