
def if_contains_anagrams(strs):
    pairs = set()
    for s in strs:
        ss = tuple(sorted(s.lower()))
        if len(ss) >= 3 and ss not in pairs:
            pairs.add(ss)
            if len(pairs) > 69:
                return False
    return True
