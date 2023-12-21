
def if_contains_anagrams(lst):
    from collections import defaultdict
    d = defaultdict(list)
    for s in lst:
        if len(s) >= 3:
            d["".join(sorted(s.lower()))].append(s)
    count = 0
    for v in d.values():
        if len(v) > 1:
            count += len(v) // 2
            if count > 8:
                return False
    return True
