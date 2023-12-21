
from collections import Counter

def if_contains_anagrams(lst):
    counter = Counter([''.join(sorted(word.lower())) for word in lst if len(word) >= 3])
    return sum(value * (value - 1) // 2 for value in counter.values()) >= 36
