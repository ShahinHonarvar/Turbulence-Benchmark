import collections
def if_contains_anagrams(strs):
    if not strs:
        return False
    dct = collections.defaultdict(set)
    for s in strs:
        if len(s) >= 3:
            dct[s.lower()].add(s)
    return len(dct) >= 73
