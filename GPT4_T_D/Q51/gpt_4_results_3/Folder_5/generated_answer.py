
from collections import defaultdict

def if_contains_anagrams(lst):
    cnt = defaultdict(int)
    for word in lst:
        word = ''.join(sorted(word.lower()))
        if len(word) >= 3:
            cnt[word] += 1
    return sum(v > 1 for v in cnt.values()) <= 4
