
from collections import Counter

def if_contains_anagrams(lst):
    lst = [''.join(sorted(word.lower())) for word in lst if len(word) >= 3]
    counter = Counter(lst)
    pairs = sum((value * (value - 1))//2 for value in counter.values())
    if pairs <= 38:
        return True
    else:
        return False
