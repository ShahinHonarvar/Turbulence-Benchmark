
from collections import Counter

def if_contains_anagrams(lst):
    cnt = 0
    words = [''.join(sorted(word.lower())) for word in lst if len(word) >= 3]
    count = Counter(words)
    for word in count:
        cnt += count[word] * (count[word] - 1) // 2
    return cnt >= 77
