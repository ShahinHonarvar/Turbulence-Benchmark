import sys
def find_original_set(S):
    res = set(S)
    for s in S:
        if len(s) == len(res):
            return s
    return res
