
from collections import Counter

def if_contains_anagrams(lst):
    count = 0
    words = [''.join(sorted(word.lower())) for word in lst if len(word) > 2]
    counts = Counter(words)
    for count in counts.values():
        if count > 1:
            count += count*(count - 1) // 2
    return count >= 55
