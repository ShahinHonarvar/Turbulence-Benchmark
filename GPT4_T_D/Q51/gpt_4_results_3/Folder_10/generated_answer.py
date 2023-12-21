
from collections import defaultdict

def if_contains_anagrams(lst_of_strings):
    anagrams = defaultdict(list)

    for s in lst_of_strings:
        s_lower = s.lower()
        if len(s_lower) >= 3:
            anagrams[''.join(sorted(s_lower))].append(s)

    count = sum(len(values) * (len(values) - 1) // 2 for values in anagrams.values())

    return count <= 21
