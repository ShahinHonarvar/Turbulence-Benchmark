
from collections import defaultdict

def if_contains_anagrams(lst):
    anagrams = defaultdict(list)
    for s in lst:
        s = s.lower()
        if len(s) >= 3:
            sorted_string = ''.join(sorted(s))
            anagrams[sorted_string].append(s)

    count = sum(len(v)*(len(v)-1)//2 for v in anagrams.values())
    return count <= 24
