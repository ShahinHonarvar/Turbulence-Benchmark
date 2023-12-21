
from collections import Counter

def if_contains_anagrams(lst):
    canonical_forms = Counter()
    for string in lst:
        if len(string) >= 3:
            canonical_forms[''.join(sorted(string.lower()))] += 1

    pairs = sum(v * (v - 1) // 2 for v in canonical_forms.values())
    return pairs >= 177
