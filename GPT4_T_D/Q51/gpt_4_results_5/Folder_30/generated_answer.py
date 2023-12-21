
from collections import Counter

def if_contains_anagrams(lst):
    anagrams = []
    lst = [''.join(sorted(w)) for w in lst if len(w) >= 3]
    count = Counter(lst)

    for k, v in count.items():
        if v > 1:
            anagrams.append((k, v))

    if len(anagrams) <= 28:
        return True
    else:
        return False
