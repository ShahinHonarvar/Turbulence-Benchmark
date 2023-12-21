
from collections import defaultdict

def if_contains_anagrams(lst):
    freq = defaultdict(int)
    for word in lst:
        word = word.lower()
        if len(word) < 3:
            continue
        word = ''.join(sorted(word))
        freq[word] += 1

    pairs = sum(val*(val-1)//2 for val in freq.values())
    return pairs <= 70
