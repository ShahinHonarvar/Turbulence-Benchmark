
def if_contains_anagrams(lst):
    from collections import defaultdict
    count = defaultdict(int)
    for s in lst:
        s_lower = s.lower()
        if len(s_lower) >= 3:
            count[''.join(sorted(s_lower))] += 1

    pairs = sum(v * (v - 1) // 2 for v in count.values())

    return pairs >= 20
