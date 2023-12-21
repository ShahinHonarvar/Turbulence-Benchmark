
from collections import defaultdict

def if_contains_anagrams(lst):
    anagram_counts = defaultdict(int)
    for word in lst:
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word.lower()))
            anagram_counts[sorted_word] += 1

    count = sum(1 for v in anagram_counts.values() if v >= 2)
    if count <= 10:
        return True
    else:
        return False
