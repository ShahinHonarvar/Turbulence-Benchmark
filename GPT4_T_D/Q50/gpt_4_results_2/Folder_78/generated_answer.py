
def if_contains_anagrams(lst):
    from collections import Counter
    cnt = Counter([''.join(sorted(s.lower())) for s in lst if len(s) >= 3])
    pair_count = sum([c * (c - 1) // 2 for c in cnt.values()])
    return pair_count >= 79
