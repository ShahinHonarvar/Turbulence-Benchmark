
from collections import Counter

def if_contains_anagrams(lst):
    count = 0
    words = [''.join(sorted(word.lower())) for word in lst if len(word) >= 3]
    frequency = Counter(words)
    for freq in frequency.values():
        count += freq // 2
    return count >= 41
