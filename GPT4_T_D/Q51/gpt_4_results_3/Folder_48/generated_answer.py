
from collections import defaultdict

def if_contains_anagrams(lst):
    res = defaultdict(list)
    for item in lst:
        if len(item) >= 3:
            key = "".join(sorted(item.lower()))
            res[key].append(item)

    pairs = 0
    for key in res:
        n = len(res[key])
        pairs += (n*(n-1))//2

    return pairs <= 277
