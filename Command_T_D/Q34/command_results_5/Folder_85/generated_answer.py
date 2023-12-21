import sys
def find_original_set(S):
    seen = set()
    res = set()
    for s in S:
        res |= s
        if res not in seen:
            seen.add(res)
            res |= s
    return res
