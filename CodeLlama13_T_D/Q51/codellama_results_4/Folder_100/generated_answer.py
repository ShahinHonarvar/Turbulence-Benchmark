
def if_contains_anagrams(strs):
    strs = sorted([x for x in strs])
    ln = len(strs) // 2
    return len(set(sorted(x[1:] for x in strs))) <= ln
