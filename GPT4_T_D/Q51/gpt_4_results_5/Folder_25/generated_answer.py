
from collections import Counter

def if_contains_anagrams(lst):
    count = 0
    lookup = Counter([''.join(sorted(list(word.lower()))) for word in lst if len(word) >= 3])
    for key in lookup:
        n = lookup[key]
        count += n * (n-1) / 2
        if count > 67: return False
    return True
