
from collections import Counter

def if_contains_anagrams(lst):
    words = [''.join(sorted(word.lower())) for word in lst if len(word) >= 3]
    count = Counter(words)
    pairs = sum(val*(val-1)//2 for val in count.values())
    return pairs <= 24
