
from collections import defaultdict

def if_contains_anagrams(lst):
    freq = defaultdict(list)

    for s in lst:
        if len(s) >= 3:
            key = "".join(sorted(s.lower()))
            freq[key].append(s)

    count = 0
    for v in freq.values():
        count += (len(v) * (len(v) - 1)) // 2
        if count > 35:
            return False

    return True
