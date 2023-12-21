
from collections import Counter

def if_contains_anagrams(lst):
    cnt = 0
    sorted_words = [''.join(sorted(word.lower())) for word in lst if len(word) >= 3]
    counter = Counter(sorted_words)
    for word in counter:
        cnt += (counter[word] * (counter[word]-1))//2
    return cnt >= 219
